def popular_words(text, words):
    text_lower = text.lower().split()

    # Count words in text
    text_word_count = {}
    for word in text_lower:
        if word in text_word_count:
            text_word_count[word] += 1
        else:
            text_word_count[word] = 1

    # Count quantity words from words in text
    word_count = {}
    for word in words:
        word_count[word] = text_word_count.get(word, 0)

    return word_count


assert popular_words(
    """When I was One I had just begun When I was Two I was nearly new """,
    ["i", "was", "three", "near"],
) == {"i": 4, "was": 3, "three": 0, "near": 0}, "Test1"
print("OK")
