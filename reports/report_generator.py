import json


def generate_report(results, output_file):

    summary = {}

    summary["avg_wer"] = sum(r["wer"] for r in results) / len(results)

    summary["avg_similarity"] = sum(
        r["similarity"] for r in results
    ) / len(results)

    summary["avg_latency"] = sum(
        r["latency"] for r in results
    ) / len(results)

    summary["hallucination_rate"] = sum(
        1 for r in results if r["hallucination"]
    ) / len(results)

    report = {
        "results": results,
        "summary": summary
    }

    with open(output_file, "w") as f:

        json.dump(report, f, indent=4)