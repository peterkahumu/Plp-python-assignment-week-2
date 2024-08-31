# creating an empty list
my_list = []

# appending elements to the list.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# inserting the value 15 at the second position of the list.
my_list.insert(1, 15)

# extending the list with another list.
my_list.extend([50, 60, 70])

# remove thelast element from the list.
my_list.pop()

# sort my list in ascending order
my_list.sort()


# find an print the index of the element 30 in the list.
index = my_list.index(30)
print(index)
