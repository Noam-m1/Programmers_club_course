def even_list(original_list):
    new_list = []
    for i in original_list:
        if i%2 == 0:
            new_list.append(i)
    return new_list
original_list = [1, 4, 5, 7, 8, 10, 13]
print(even_list(original_list))
