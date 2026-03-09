def detect_hallucination(similarity_score, threshold):

    if similarity_score < threshold:
        return True

    return False