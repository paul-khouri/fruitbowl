names = ["Alice","Belinda", "Chansing", "Debbie", "Eloise", "Floss"]
# view the list
# view the list with a counter
# find how many elements are in the list
# remove an elements from a list
# access an element in a list


# loop through list
for x in names:
    print(x, end="")
print()
# loop using a counter
for i in range(0, len(names)):
    print(i)
names.remove("Alice")
print(names)
names.append("Alice")
print(names)
names.sort()
print(names)
del names[3]
print(names)
print(names.pop(0))
print(names)


