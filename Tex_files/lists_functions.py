import random
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

def insert_at_index(L):
    choice = int(input("Enter index number to insert at:  ->  "))
    value = input("Enter value to insert: ->  ")
    L.insert(choice , value)
    print_with_indexes(L)
    return L

def shuffle_list(L):
    random.shuffle(L)
    print_with_indexes(L)


def sort_list(L):
    L.sort()
    print_with_indexes(L)

def find_in_list(L):
    value = input("Who would you like find? ->  ")
    if value in L:
        my_string = "{} is in the list and it is at index #{}".format(value, L.index(value))
    else:
        my_string = "{} is not in the list".format(value)
    print(my_string)




def main():
    names = ["Alice", "Belinda", "Chansing", "Debbie", "Eloise", "Floss"]
    run = True
    while run:
        print("-"*50)
        menu = {
            "A" : "Print a list horizontally",
            "B" : "Print a list vertically with indexes",
            "C" : "Remove and item from the list",
            "D" : "Add an item",
            "E" : "Remove an item at a specified index",
            "F" : "Insert an item at a given index",
            "G" : "Sort the list",
            "H" : "Find an item in the list",
            "I" : "Shuffle List",
            "Q" : "Quit"
        }
        i = 0
        menu_string = ""
        for x, y in menu.items():
            menu_string += "| {:2} - {:50} ".format(x,y)
            i += 1
            if i != 0 and i%2 == 0:
                menu_string += "\n"
        print(menu_string)

        choice = input("Please enter your choice: -> ")
        print("-" * 50)
        if choice == "A":
            print_list(names)
        elif choice == "B":
            print_with_indexes(names)
        elif choice ==  "C":
            remove_item(names)
        elif choice == "D":
            add_to_list(names)
        elif choice == "E":
            remove_at_index(names)
        elif choice == "F":
            insert_at_index(names)
        elif choice == "G":
            sort_list(names)
        elif choice == "H":
            find_in_list(names)
        elif choice == "I":
            shuffle_list(names)
        elif choice =="Q":
            print("Thanks , you have quit")
            run = False
        else:
            print("Your entry has not been recognised")


main()