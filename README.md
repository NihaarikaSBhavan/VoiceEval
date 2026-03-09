# Voice AI Evaluation Framework

## Overview

**Voice AI Evaluation Framework** is a modular Python system for evaluating speech-based AI systems.
It analyzes audio responses, transcribes them using a speech-to-text model, and evaluates the output using multiple metrics such as transcription accuracy, semantic similarity, latency, and hallucination detection.

This project is designed for **researchers, developers, and ML engineers** who want to benchmark voice AI pipelines or evaluate spoken responses in interview-style datasets.

The framework supports:

* Audio transcription
* LLM-based response analysis
* Evaluation metrics
* Dataset validation
* Automated report generation



## Project Architecture


voice_ai_eval/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── dataset.json
│   └── audio/
│       ├── q1.mp4
│       └── q2.mp4
│
├── transcription/
│   └── whisper_engine.py
│
├── llm/
│   └── ollama_client.py
│
├── metrics/
│   ├── wer_metric.py
│   ├── semantic_similarity.py
│   ├── latency.py
│   └── hallucination.py
│
├── evaluator/
│   ├── dataset_validator.py
│   └── evaluation_pipeline.py
│
└── reports/
    └── report_generator.py




## Features

### 1. Speech Transcription

Uses **Faster-Whisper** to convert audio responses into text.

Supported formats:

* `.wav`
* `.mp3`
* `.m4a`
* `.mp4`

### 2. Evaluation Metrics

The system evaluates AI responses using multiple metrics:

**Word Error Rate (WER)**
Measures transcription accuracy.

**Semantic Similarity**
Uses sentence embeddings to compare the transcript with the reference answer.

**Latency**
Measures the time required to process the audio input. (Latency observed depends on the infrastructure you are working on)

**Hallucination Detection**
Uses a threshold on the similarity score to detect whether the response contains fabricated or unrelated information.

### 3. Dataset Validation

Ensures that:

* Audio files exist
* Required dataset fields are present
* Paths are correct

### 4. Automated Evaluation Pipeline

The pipeline processes multiple samples in parallel and calculates evaluation metrics automatically.

### 5. Report Generation

After evaluation, results are saved as structured reports.



## Dataset Format

The dataset is stored in:


data/dataset.json


Example format:

json

    {
      "tests": [
        {
          "audio": "q1.mp4",
          "ground_truth_transcript": "what is the capital of france",
          "expected_answer": "Paris is the capital of France."
        },
        {
          "audio": "q2.mp4",
          "ground_truth_transcript": "who discovered gravity",
          "expected_answer": "Isaac Newton discovered gravity."
        }
      ]
    }


Fields:

            

 audio                   - Unique sample identifier
 
 ground_truth_transcript - Ground truth reference text 
 
 expected_answer         - answer to be expected       



## Installation

### 1. Clone the Repository


git clone <repo_url>
cd voice_ai_eval


### 2. Create Virtual Environment


python -m venv venv


Activate:

Windows


venv\Scripts\activate


Mac/Linux


source venv/bin/activate


### 3. Install Dependencies


pip install -r requirements.txt




## Model Setup

The project uses:

* **Faster-Whisper** for transcription
* **Sentence Transformers** for semantic similarity
* **Ollama** for LLM-based hallucination detection

Install Ollama:

https://ollama.com/download

Pull a model:


ollama pull llama3

Test model:


ollama run llama3


## Running the Evaluation

From the project root directory:


python3 main.py


The pipeline will:

1. Load the dataset
2. Transcribe each audio file
3. Compute evaluation metrics
4. Generate a report



## Example Output

        {
            "audio": "q1.mp4",
            "transcript": "What is the capital of France?",
            "response": "The capital of France is Paris.",
            "wer": 0.3333333333333333,
            "similarity": 0.9893566370010376,
            "latency": 160.71692538261414,
            "hallucination": false
        }

## Generated Reports




Example output:


evaluation_report.json


Example structure:

json

{
    "results": [
        {
            "audio": "q1.mp4",
            "transcript": "What is the capital of France?",
            "response": "The capital of France is Paris.",
            "wer": 0.3333333333333333,
            "similarity": 0.9893566370010376,
            "latency": 160.71692538261414,
            "hallucination": false
        },
        {
            "audio": "q2.mp4",
            "transcript": "Who discovered gravity?",
            "response": "Gravity was not discovered by a single person. Instead, it was a concept that was developed and understood through the work of many scientists and philosophers over the centuries.\n\nThe ancient Greeks, such as Aristotle and Archimedes, were among the first to discuss the concept of gravity. Aristotle believed that objects have a natural tendency to move towards their natural place, which was thought to be the center of the universe. Archimedes, on the other hand, was one of the first to describe the concept of gravity as a force that pulls objects towards each other.\n\nIn the 17th century, Sir Isaac Newton developed the law of universal gravitation, which states that every point mass attracts every other point mass by a force acting along the line intersecting both points. This law, which is now known as the law of gravity, was first presented in Newton's groundbreaking book \"Philosophi\u00e6 Naturalis Principia Mathematica\" in 1687.\n\nNewton's law of gravity was a major breakthrough in understanding the natural world, and it laid the foundation for the development of modern physics. However, it was not until the 20th century that the concept of gravity was fully understood and described by Albert Einstein's theory of general relativity.\n\nEinstein's theory, which was developed in the early 20th century, describes gravity as the curvature of spacetime caused by the presence of mass and energy. According to this theory, the more massive the object, the more it warps the fabric of spacetime around it, and the stronger the gravitational pull it exerts on other objects.\n\nIn summary, while it is difficult to identify a single person who \"discovered\" gravity, the concept of gravity has been developed and understood through the work of many scientists and philosophers over the centuries, from the ancient Greeks to Newton and Einstein.",
            "wer": 0.6666666666666666,
            "similarity": 0.6805293560028076,
            "latency": 609.0017385482788,
            "hallucination": true
        }
    ],
    "summary": {
        "avg_wer": 0.5,
        "avg_similarity": 0.8349429965019226,
        "avg_latency": 384.8593319654465,
        "hallucination_rate": 0.5
    }
}


## Key Components

### Whisper Engine

Handles audio transcription using Faster-Whisper.


.transcription/whisper_engine.py


### Evaluation Pipeline

Coordinates transcription, metrics, and reporting.


evaluator/evaluation_pipeline.py


### Metrics Module

Implements evaluation algorithms.


.metrics/


### LLM Client

Handles interactions with Ollama models.


.llm/ollama_client.py


### Report Generator

Generates structured evaluation reports.


.reports/report_generator.py




## Extending the Framework

You can easily add additional metrics by creating new modules in the `metrics` directory.

Examples:

* Fluency score
* Grammar evaluation
* Speech rate
* Filler word detection
* Pronunciation scoring



## Use Cases

* Voice AI benchmarking
* Speech recognition evaluation
* AI interview systems
* Conversational AI research
* Audio dataset evaluation



## Future Improvements

Planned enhancements include:

* Real-time streaming evaluation
* Speaker diarization
* Multi-language support
* Visualization dashboards
* Batch audio processing



## License

This project is intended for educational and research purposes.



## Author
Nihaarika Saravana Bhavan (Applied AI/ML Engineer)
Developed as a modular framework for evaluating voice-based AI systems using modern speech recognition and language models.
