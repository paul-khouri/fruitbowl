def get_string(m):
    my_string = input(m)
    return my_string

def get_integer(message):
    my_integer = int(input(message))
    return my_integer

def print_with_indexes(L):
    for i in range(0, len(L)):
        output ="{:3} : {:10} {:10} {:10}".format(i,L[i][0], L[i][1], L[i][2])
        print(output)


def single_loop_print(L):
    """ This prints out the multidimensional list
     so that the complete contents can be seen
     returns none """
    for i in range(0, len(L)):
        output = "{:10} ---   {:10}  ---  {:<10}".format(L[i][0], L[i][1], L[i][2] )
        print(output)

def add_new_entry(L):
    """ Takes a multidimension list with inner list length 3
    adds a new list
    return none"""
    print("Start adding new entry.")
    name = get_string("Please enter the new name: -> ")
    hair_colour = get_string("Please enter hair colour: -> ")
    age = get_integer("Please enter age: -> ")
    new_list = [name, hair_colour, age ]
    L.append(new_list)

def update_name(L):
    print_with_indexes(L)
    my_index = int(input("Choose option number for name to update: -> "))
    new_name = input("Enter new name: -> ")
    old_name = L[my_index][0]
    L[my_index][0]= new_name
    my_string = "The name for {} has been updated to {}".format(old_name,L[my_index][0])
    print(my_string)
    return None


def update_hair(L):
    print_with_indexes(L)
    my_index = int(input("Choose option number for hair to update: -> "))
    new_colour = input("Enter new hair colour: -> ")
    L[my_index][1]= new_colour
    my_string = "The hair colour for {} has been updated to {}".format(L[my_index][0],L[my_index][1])
    print(my_string)
    return None


def update_age(L):
    print_with_indexes(L)
    my_index = int(input("Choose option number for age to update: -> "))
    new_age = int(input("Enter new age: -> "))
    L[my_index][2]= new_age
    my_string = "The age for {} has been updated to {}".format(L[my_index][0],L[my_index][2])
    print(my_string)
    return None



def update(L):
    menu = [
        ("N", "Name"),
        ("H", "Hair"),
        ("A", "Age")
    ]
    for i in range(0, len(menu)):
        print( "{} {}".format(menu[i][0],menu[i][1] ) )
    option = get_string("Please choose option to update: -> ")
    if option == "N":
        update_name(L)
    elif option == "H":
        update_hair(L)
    elif option == "A":
        update_age(L)
    else:
        print("Unrecognised entry")


def search(L):
    item = get_string("Please choose search item: -> ")
    # creating a variable ffound and initilise as false
    not_found = True
    for i in range(0, len(L)):
        for j in range(0,len(L[i])):
            if item == str(L[i][j]):
                print("Found it {} is at Row {} Column {}".format(item , i, j))
                print(L[i])
                # something has now be found so change to True
                not_found = False
    if not_found == True:
        print("Your item could not be found")



def menu():
    my_L =[
        ["Alice", "Blond", 12],
        ["Cathy", "Blond", 15],
        ["Dan", "Black", 10],
        ["Bob", "Brown", 13],
        ["Joe", "Green", 13]
    ]
    my_menu = [
        ("R", "Review"),
        ("U", "Update"),
        ("A", "Add new name"),
        ("S", "Search"),
        ("Q", "Quit")
    ]
    run = True
    while run == True:
        # printing main menu
        for i in range(0, len(my_menu)):
            print("{:3} : {}". format(my_menu[i][0], my_menu[i][1]))
        option = get_string("Please choose option: - > ")
        if option == "R":
           single_loop_print(my_L)
        elif option == "U":
            update(my_L)
        elif option == "A":
            add_new_entry(my_L)
        elif option == "S":
            search(my_L)
        elif option == "Q":
            print("Quit")
            run = False
        else:
            print("Invalid Entry")




menu()


