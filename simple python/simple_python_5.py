str = "Hello world"
count_vowels = 0
for i in range (len(str)):
    if str[i] in "aeoiuAEOIU":
        count_vowels += 1
print(count_vowels)