import argparse
import config

from evaluator.evaluation_pipeline import EvaluationPipeline
from reports.report_generator import generate_report


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--dataset", default=config.DATASET_PATH)
    parser.add_argument("--model", default=config.MODEL_NAME)

    args = parser.parse_args()

    config.DATASET_PATH = args.dataset
    config.MODEL_NAME = args.model

    pipeline = EvaluationPipeline()

    results = pipeline.run()

    generate_report(results, config.OUTPUT_REPORT)

    print("Evaluation complete")
    print("Report saved to:", config.OUTPUT_REPORT)


if __name__ == "__main__":
    main()