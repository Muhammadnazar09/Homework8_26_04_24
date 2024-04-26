my_dict = {
    "name": "muhammad",
    "age": 22,
    "salary": 5000,
    "city": "dushanbe"
}
key = ["name", "salary"]
for i in key:
    my_dict.pop(i)
print(my_dict)