from knowledge_base import knowledge_base


def get_response(question):
    question = question.lower().strip()

    # Remove common punctuation
    punctuation = "?!.,"
    for symbol in punctuation:
        question = question.replace(symbol, "")

    # Direct keyword matching
    for key, answer in knowledge_base.items():
        if key in question:
            return answer

    # Flexible matching for common question words
    words = question.split()

    for key, answer in knowledge_base.items():
        key_words = key.split()

        if any(word in words for word in key_words if len(word) > 3):
            return answer

    return "Sorry, I don't know the answer to that question yet."