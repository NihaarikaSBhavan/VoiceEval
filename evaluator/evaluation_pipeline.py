import json
import os

from concurrent.futures import ThreadPoolExecutor

import config

from transcription.whisper_engine import WhisperEngine
from llm.ollama_client import OllamaClient

from metrics.wer_metric import compute_wer
from metrics.semantic_similarity import compute_similarity
from metrics.latency import measure_latency
from metrics.hallucination import detect_hallucination

from evaluator.dataset_validator import validate_dataset


class EvaluationPipeline:

    def __init__(self):

        self.whisper = WhisperEngine(config.WHISPER_MODEL)

        self.llm = OllamaClient(config.MODEL_NAME)

    def evaluate_test(self, test):

        audio_path = os.path.join(
            config.AUDIO_FOLDER,
            test["audio"]
        )

        transcript = self.whisper.transcribe(audio_path)

        wer_score = compute_wer(
            test["ground_truth_transcript"],
            transcript
        )

        response, latency = measure_latency(
            self.llm.generate,
            transcript
        )

        similarity = compute_similarity(
            test["expected_answer"],
            response
        )

        hallucination = detect_hallucination(
            similarity,
            config.SIMILARITY_THRESHOLD
        )

        return {
            "audio": test["audio"],
            "transcript": transcript,
            "response": response,
            "wer": wer_score,
            "similarity": similarity,
            "latency": latency,
            "hallucination": hallucination
        }

    def run(self):

        with open(config.DATASET_PATH) as f:

            dataset = json.load(f)

        validate_dataset(dataset)

        with ThreadPoolExecutor(max_workers=4) as executor:

            results = list(
                executor.map(
                    self.evaluate_test,
                    dataset["tests"]
                )
            )

        return results