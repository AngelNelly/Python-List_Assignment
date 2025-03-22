my_list = [] # empty list


my_list.append(100) # I used append to add 100 to 200 to the list
my_list.append(200)
my_list.append(300)
my_list.append(400)
print(my_list)


my_list.insert(500, 600) # I used insert to add 500 to 600 to the list
print(my_list)


my_list.extend([700, 800, 900, 1000]) # I used extend to add 700 to 1000 to the list
print(my_list)

my_list.pop(8) # I used pop to remove 1000 from the list
print(my_list)

my_list.sort(reverse=True) # I used sort to sort the list in descending order, from 900 to 100. If I used just "sort",
print(my_list) #It will remain in ascending order so I decided to use "sort(reverse=True)" to sort it in descending order.