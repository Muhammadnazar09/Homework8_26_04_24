my_dictionary1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
my_dictionary2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
for i in my_dictionary2.keys():
    my_dictionary1[i] = my_dictionary2[i]
print(my_dictionary1)

# my_dictionary3 = my_dictionary1 | my_dictionary2
# print(my_dictionary3)