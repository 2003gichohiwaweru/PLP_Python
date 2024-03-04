my_list = []

#appends thos valus
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#inserts 15 value in the second position
my_list.insert(1, 15)

print(my_list)

#Extends another list
my_list.extend([50, 60, 70])
print(my_list)

#Removes the last character
my_list.pop()
print(my_list)

my_list.sort()

index_30 = my_list.index(30)
print ("The index of 30 is: ", index_30)

print("The final list: ", my_list)