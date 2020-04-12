names = ["Alice","Belinda", "Chansing", "Debbie", "Eloise", "Floss"]

def print_list(L):
    my_string = ""
    for x in L:
        my_string =  my_string + x + " , "
    print(my_string)

def print_with_indexes(L):
    for i in range(0,len(L)):
        output = "{} : {}".format(i, L[i])
        print(output)


def remove_item(L):
    print_list(L)
    choice = input("Who would you like to remove?  ")
    if choice in L:
        L.remove(choice)
        print("{} has been removed".format(choice))
    else:
        print("You choice is not in the list")
    print_list(L)


def add_to_list(L):
    print_list(L)
    choice = input("Who would you like to add?  ")
    L.append(choice)
    print_list(L)

def remove_at_index(L):
    print_with_indexes(L)
    choice = int(input("Enter index number to remove:   "))
    if 0 <= choice < len(L):
        del L[choice]
        print_with_indexes(L)
    else:
        print("This is not a valid index number")

def sort_list(L):
    L.sort()
    print_with_indexes(L)



#print_list(names)
remove_item(names)
#print_with_indexes(names)
#remove_at_index(names)
#add_to_list(names)
#sort_list(names)