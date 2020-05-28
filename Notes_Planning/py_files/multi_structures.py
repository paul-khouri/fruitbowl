def get_integer(m):
    my_integer = int(input(m))
    return my_integer

def get_string(m):
    my_string = input(m)
    return my_string


def loop_on_lists(L):
    print("-" * 30)
    c = 0
    for x in L:
        my_string = "{:2}: {:5} , {:5} , {:^5}".format(c, x[0], x[1], x[2])
        print(my_string)
        c+=1
    print("-" * 30)
    return None

def update_name(L):
    loop_on_lists(L)
    my_index = int(input("Choose option number for name to update: -> "))
    new_name = input("Enter new name: -> ")
    old_name = L[my_index][0]
    L[my_index][0]= new_name
    my_string = "The name for {} has been updated to {}".format(old_name,L[my_index][0])
    print(my_string)
    return None


def update_hair(L):
    loop_on_lists(L)
    my_index = int(input("Choose option number for hair to update: -> "))
    new_colour = input("Enter new hair colour: -> ")
    L[my_index][1]= new_colour
    my_string = "The hair colour for {} has been updated to {}".format(L[my_index][0],L[my_index][1])
    print(my_string)
    return None


def update_age(L):
    loop_on_lists(L)
    my_index = int(input("Choose option number for age to update: -> "))
    new_age = int(input("Enter new age: -> "))
    L[my_index][2]= new_age
    my_string = "The age for {} has been updated to {}".format(L[my_index][0],L[my_index][2])
    print(my_string)
    return None


def update(L):
    update_menu = [
        ("N", "Name"),
        ("H", "Hair"),
        ("A", "Age"),
        ("B", "Back")
    ]
    for x in update_menu:
        print( "{} : {}".format(x[0],x[1]))
    choice = input("Please enter your option letter: -> ")
    if choice is "N":
        update_name(L)
    elif choice is "H":
        update_hair(L)
    elif choice is "A":
        update_age(L)
    elif choice is "B":
        print("Returning to main menu")
        return None
    else:
        print("Unrecognised Entry")
    return None


def search_lists(L):
    search_item = input("Please enter your search item: -> ")
    try:
        s= int(search_item)
    except:
        s = search_item
    row = 0
    for y in L:
        if s in y:
            item_index = y.index(s)
            print("{} has been found at Row {} index {}".format( y[item_index],row,  item_index ) )
        row += 1
    return None


def create_new_entry(L):
    name = input("Please enter name: -> ")
    hair_colour = input("Please enter hair colour: -> ")
    age = int(input("Please enter age: -> "))
    L.append( [name, hair_colour , age])
    return None


def sort_on_index(L,H):
    for i in range(0, len(H)):
        print( "{} : {}".format(i, H[i]))
    sort_index = int(input(" Please choose index to sort on: -> "))
    L = sorted(L, key = lambda x: x[sort_index])
    return L


def menu():
    group_of_lists_header = ["Name", "Hair", "Age"]
    group_of_lists =[
        ["Alice", "Blond", 12],
        ["Cathy", "Blond", 15],
        ["Dan", "Black", 10],
        ["Bob", "Brown", 13],
        ["Joe", "Green", 13]
    ]

    my_menu = [
        ("R", "Review"),
        ("U", "Update"),
        ("S", "Search"),
        ("A", "Add new name"),
        ("O", "Order"),
        ("Q", "Quit")
    ]

    run = True
    while run is True:
        for x in my_menu:
            print( "{} : {}".format(x[0],x[1]))
        print("-"*30)
        choice = input("Please enter your option letter: -> ")
        if choice is "R":
            loop_on_lists(group_of_lists)
        elif choice is "U":
            update(group_of_lists)
        elif choice is "S":
            search_lists(group_of_lists)
        elif choice is "A":
            create_new_entry(group_of_lists)
        elif choice is "O":
            group_of_lists = sort_on_index(group_of_lists, group_of_lists_header)
        elif choice is "Q":
            print("Thank you")
            run = False
        else:
            print("Unrecognised Entry")
    return None


if __name__ == "__main__":
    menu()






