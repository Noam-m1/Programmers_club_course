def find_palindromes(words):
    palindromes = []
    for i in words:
        same = True
        if len(i)%2 == 0:
            for j in range((int)(len(i)/2)):
                if i[j] != i[-j-1]:
                    same = False
                    break
        else:
            for j in range((int)((len(i)-1)/2)):
                if i[j] != i[-j-1]:
                    same = False
                    break
        if same == True:
            palindromes.append(i)
    return palindromes

words = ["radar", "level", "apple", "what", "bananna", "stats", "noon"]
print(find_palindromes(words))