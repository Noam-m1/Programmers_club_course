def file_longest_word(file):
    dictionary = {}
    with open(file, 'r') as file:
        for line in file:
            for word in line.split():
                if word in dictionary:
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1
    return sorted(dictionary.items(), key=lambda item: item[1], reverse=True)

def how_many_words (N, file):
    dictionary = list(file_longest_word(file))
    for word in range(N):
        print(dictionary[word])

filepath = input("please enter your desired filepath:")
how_many_words(3, filepath)

