def find_longest_word(words):
    longest_words = [words[0]]
    for i in words:
        if len(longest_words[0]) < len(i):
            longest_words = [i]
            continue
        if len(longest_words[0]) == len(i):
            longest_words.append(i)
    return longest_words

words = ["boy", "girl", "hi", "what", "child", "cross", "books"]
print(find_longest_word(words))