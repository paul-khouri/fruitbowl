
def loop_on_lists(L):
    print("-" * 30)
    c = 0
    for x in L:
        if c == 0:
            my_string = "{:2}  {:5} , {:5} , {:^5}\n" \
                        "{:2}  {:5}  {:5}  {:5}" \
                        " ".format("", x[0], x[1], x[2],"",  "-"*5 ,  "-"*5,  "-"*5)
        else:
            my_string = "{:2}: {:5} , {:5} , {:^5}".format(c, x[0], x[1], x[2])
        print(my_string)
        c+=1

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
    M = L[0]
    for i in range(1, len(M)):
        print("{} : {}".format(i, M[i]))
    choice = int(input("Please enter your option letter: -> "))
    if choice is 1:
        update_hair(L)
    elif choice is 2:
        update_age(L)
    else:
        print("Unrecognised Entry")


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

def create_new_entry(L):
    name = input("Please enter name: -> ")
    hair_colour = input("Please enter hair colour: -> ")
    age = int(input("Please enter hair colour: -> "))
    L.append( [name, hair_colour , age])
    loop_on_lists(L)

def sort_on_index(L):
    loop_on_lists(L)
    for i in range(0, len(L[0])):
        print( "{} : {}".format(i, L[0][i]))
    sort_index = int(input(" Please choose index to sort on: -> "))
    M = L.pop(0)
    L=sorted(L, key = lambda x: x[sort_index])
    L.insert(0,M)
    loop_on_lists(L)
    return L

def menu(group_of_lists):

    my_menu = [
        ("R", "Review"),
        ("U", "Update"),
        ("S", "Search"),
        ("A", "Add new name"),
        ("O", "Order"),
        ("Q", "Quit")
    ]
    print("-" * 30)
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
        group_of_lists = sort_on_index(group_of_lists)
    elif choice is "Q":
        print("Thank you")
        return "Q"
    else:
        print("Unrecognised Entry")
    return group_of_lists


def main():
    group_of_lists_header = ["Name", "Hair", "Age"]
    group_of_lists =[
        group_of_lists_header,
        ["Alice", "Blond", 12],
        ["Cathy", "Blond", 15],
        ["Dan", "Black", 10],
        ["Bob", "Brown", 13],
        ["Joe", "Green", 13]
    ]
    run = True
    while run:
        status = menu(group_of_lists)
        if status == "Q":
            run = False
        else:
            group_of_lists = status
main()






