my_dictionary1=['Kelly','Emma']
my_dictionary2={"designation":'Developer',"salary":8000}
new_dictionary={}
for i in my_dictionary1:
    new_dictionary[i]=my_dictionary2.copy()
print(new_dictionary)