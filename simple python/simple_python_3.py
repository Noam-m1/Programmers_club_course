order_list = True
test_list = [1, 2, 3, 4, 5]
for i in range (len(test_list)-1):
    if test_list[i+1] < test_list[i]:
        order_list = False
print(order_list)
