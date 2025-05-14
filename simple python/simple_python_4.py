str = "Hello world"
new_str = ""
for i in range(len(str)):
    new_str += str[-i-1]
print(new_str)