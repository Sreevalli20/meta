def grade(response: str, expected_keywords):
    score = 0
    for word in expected_keywords:
        if word.lower() in response.lower():
            score += 1
    return min(score / len(expected_keywords), 1.0)
