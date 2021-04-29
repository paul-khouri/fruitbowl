"""Fruitbowl management program."""
from difflib import SequenceMatcher


def similar(a, b):
    """Return matcher ratio.

    :param a: str
    :param b: str
    :return: float

    returns a ratio computed from how much one string matches another.
    a ratio of 1 is a perfect match
    """
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def make_dotted_line():
    print("-"*20)


def get_integer(m, min_, max_):
    """Return validated bounded integer.

    :param m: str
    :param min_: int
    :param max_: int
    :return: int
    """
    cont = "y"
    while cont == "y":
        try:
            my_integer = int(input(m))
        except ValueError:
            print("please enter an integer value")
            continue
        if my_integer < min_:
            print("The value you have entered is too low")
            continue
        elif my_integer > max_:
            print("The value you have entered is too high")
            continue
        return my_integer


def get_string(message, max_):
    """Return string validated by length.

    :param message: str
    :param max_: int
    :return: str
    """
    cont = "y"
    while cont == "y":
        response_string = input(message)
        if len(response_string) < 1:
            print("No proper fruit name has been entered")
            continue
        elif len(response_string) > max_:
            print("Too many characters for a fruit name")
            continue
        else:
            return response_string


def print_fuits_with_options(f):
    """Print list with index numbers.

    :param f: list
    :return: None
    """
    for i in range(0, len(f)):
        my_string = "{:<5}{:10}".format(i, f[i][0])
        print(my_string)


def current_fruit_bowl(f):
    """Print list of fruit.

    :param f: list
    :return: None
    """
    print("{:20}{:<20}".format("Fruit","Pieces of:"))
    for i in f:
        my_fruit = "{:20}{:<20}".format(i[0], i[1])
        print(my_fruit)


def add_fruit(f):
    """Add extra fruit to pre-existing fruit.
    
    :param f: 
    :return: 
    """
    print("-" * 60)
    # print formatted list with indices
    for i in range(0, len(f)):
        my_string = "{:<5}{:10}".format(i, f[i][0])
        print(my_string)
    print("-" * 60)
    # request index number and quantity to add
    option = get_integer("Choose option number of fruit to add: -->  ", 0, len(f))
    my_amount = get_integer("How many {} would you like to add? -->  ".format(f[option][0]), 0, 10)
    # add to existing amount
    f[option][1] = f[option][1]+my_amount
    response_string = "You now have {} {} in the fruitbowl".format(f[option][1], f[option][0])
    print(response_string)


def eat_fruit(f):
    """Remove count of fruit from chosen sublist.

    :param f: list
    :return: None
    """
    print("-" * 60)
    # print formatted list with indices
    for i in range(0, len(f)):
        my_string = "{:<5}{:10}".format(i, f[i][0])
        print(my_string)
    print("-" * 60)
    # request index number and quantity to add
    option = get_integer("Choose option number of fruit to eat -- > ", 0, len(f))
    # validate subtraction amount to ensure we cannot end up with negative fruit
    my_amount = get_integer("How many {} would you like to eat -- > ?".format(f[option][0]), 0, f[option][1])
    # subtract from existing amount
    f[option][1]=f[option][1]-my_amount
    response_string = "You now have {} {} in the fruitbowl".format(f[option][1], f[option][0])
    print(response_string)


def add_up_fruit(F):
    """Print the total sum of fruit pieces.
    
    :param F: list
    :return: None

    requires row and column list
    """
    total_fruit = 0
    for i in range(0, len(F)):
        total_fruit += total_fruit + F[i][1]
    print("You have {} pieces of fruit in the fruit bowl".format(total_fruit))

def new_fruit(F):
    cont = "y"
    while cont == "y":
        change = False
        fruit_name = get_string("Please enter the name of your fruit:", 20)
        # this needs to be checked against pre-existing entries
        checked_name = check_new_name(fruit_name,F)
        if checked_name != fruit_name:
            fruit_name = checked_name
            change = True
        fruit_amount = get_integer("Please enter how much fruit you have:",0,10)

        print( "You have entered {} with {} pieces".format(fruit_name, fruit_amount) )
        confirm = input("press (y) to confirm, (n) to re-enter again or (e) to exit without changes")
        if confirm == "y":
            if change == True:
                add_fruit_name_quantity(F, fruit_name.lower(), fruit_amount)
            else:
                F.append([fruit_name, fruit_amount])
            return
        elif confirm == "n":
            continue
        elif confirm == "e":
            return
        else:
            print("not a valid entry")
            continue



def add_fruit_name_quantity(L,n,q):
    update = False
    for i in range(0,len(L)):
        if n == L[i][0]:
            L[i][1]+=q
            update = True
    if update == False:
        print("Error on add fruit name quantity")
        return False
    return True


# check if fruit is already in the list
def check_new_name(n, L):
    for x in L:
        r=similar(x[0], n)
        if r > 0.6:
            output = "Your entry of {} closely matches a prexisting entry of {}".format(n, x[0])
            print(output)
            choice = get_string("Enter y to use your entry or n to use the prexisting fruit (y/n): -> ",10)
            if choice == "y":
                return n
            elif choice == "n":
                return x[0]
            else:
                print("unknown entry")
    return n


def get_option(F):
    print("-"*60)
    print("Choose your option")
    options_list = [
        ["A", "Add fruit"],
        ["E", "Eat fruit"],
        ["R", "Review fruit"],
        ["T", "Total fruit"],
        ["N", "New fruit"],
        ["Q", "Quit"]
    ]
    for i in range(0, len(options_list)):
        my_options ="{:3}{:10}".format(options_list[i][0], options_list[i][1])
        print(my_options)
    print("-" * 60)
    option = input("Please choose your option: -> ")
    if option == "A":
        add_fruit(F)
        return
    elif option == "E":
        eat_fruit(F)
        return
    elif option == "R":
        current_fruit_bowl(F)
        return
    elif option == "T":
        add_up_fruit(F)
        return
    elif option == "N":
        new_fruit(F)
        return
    elif option == "Q":
        return option
    else:
        print("Not an option")

def main():
    fruit_bowl = [
        ["apples", 0],
        ["pears", 0],
        ["quinces", 0],
        ["lemons", 0]
    ]
    cont = "y"
    current_fruit_bowl(fruit_bowl)
    while cont=="y":
        response = get_option(fruit_bowl)
        if response == "Q":
            cont = "n"


if __name__ == "__main__":
    main()


