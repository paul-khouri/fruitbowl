import random
def get_integer(m):
    my_integer = int(input(m))
    return my_integer


def get_string(m):
    my_string = input(m)
    return my_string


def print_at_index(L):
    my_index = get_integer("Please enter index number: -> ")
    output = "The value --  {} -- is at index {} in the list".format(L[my_index], my_index)
    print(output)
    print("." * 100)


def print_list(L):
    for x in L:
        print(x)
    print("." * 100)


def print_list_indexes(L):
    for i in range(0, len(L)):
        print( "{} : {}".format(i, L[i]))
    print("." * 100)


def add_item(L):
    my_item = get_string("Please enter new item: -> ")
    L.append(my_item)


def find_item(L):
    item = get_string("Who do you want to find? -> ")
    if item in L:
        index_num = L.index(item)
        output = "{} has been found is at index number {}".format(L[index_num], index_num)
        print(output)
    else:
        print("{} is not is the list".format(item))
    print("." * 100)


def remove_item(L):
    item = get_string("Who do you want to remove? -> ")
    if item in L:
        L.remove(item)
        output = "{} has been removed from the list".format(item)
        print(output)
    else:
        print("{} could not be found".format(item))
    print("." * 100)


def sort_list(L):
    L.sort()

def shuffle_list(L):
    random.shuffle(L)



def change_value(L):
    # print menu so user has index numbers
    print_list_indexes(L)
    index_num = get_integer("Please choose the index number: -> ")
    new_value = get_string("Please enter new value: -> ")
    # we now have all the values we need
    # temporarily hold old value for print out
    old_value = L[index_num]
    # update value
    L[index_num]= new_value
    # confirmation message
    output = "The old value of {} is now changed to {}".format(old_value, L[index_num])
    print(output)


def menu():
    my_list_one = ["Mary", "Patsy", "Jean", "Constantine", "Pierre"]
    my_list_two = ["Bob", "Ron", "Max", "Joe", "Pat"]
    my_list = my_list_two
    print("my_list is currently set to: {}".format(my_list))
    my_menu='''
    A: print the list
    B: print the list with indices
    C: add item to list
    D: print at index number
    E: change value in the list
    F: Choose list 1
    G: Choose list 2
    H: Find item in list
    I: Remove item from list
    J: Sort List
    K: Shuffle list
    Q: Quit
    '''
    print(id(my_list_one))
    print(id(my_list_two))
    print(id(my_list))



    run = False
    while run == True:
        print(my_menu)
        choice = get_string("Please select you option: -> ").upper()
        print("."*100)
        if choice == "A":
            print_list(my_list)
        elif choice == "B":
            print_list_indexes(my_list)
        elif choice == "C":
            add_item(my_list)
        elif choice == "D":
            print_at_index(my_list)
        elif choice == "E":
            change_value(my_list)
        elif choice == "F":
            my_list = my_list_one
            print("my_list ONE is now selected")
        elif choice == "G":
            my_list = my_list_two
            print("my_list TWO is now selected")
        elif choice == "H":
            find_item(my_list)
        elif choice == "I":
            remove_item(my_list)
        elif choice == "J":
            sort_list(my_list)
        elif choice == "K":
            shuffle_list(my_list)
        elif choice == "Q":
            print("Thank you")
            run = False
        else:
            print("Invalid entry")


menu()