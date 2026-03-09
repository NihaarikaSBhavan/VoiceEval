REQUIRED_FIELDS = [
    "audio",
    "ground_truth_transcript",
    "expected_answer"
]


def validate_dataset(dataset):

    for i, test in enumerate(dataset["tests"]):

        for field in REQUIRED_FIELDS:

            if field not in test:

                raise ValueError(
                    f"Missing field '{field}' in test case {i}"
                )