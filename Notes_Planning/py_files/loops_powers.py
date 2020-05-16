
def square(s,e):
    c = s
    while c <= e:
        my_string = "{:<6} {}".format(c, c*c)
        print(my_string)
        c += 1


def cube(s,e):
    c = s
    while c <= e:
        my_string = "{:<6} {}".format(c, c*c*c)
        print(my_string)
        c += 1



def get_integer_input(m):
    my_number = int(input(m))
    return my_number

def get_string_input(m):
    my_letter = input(m)
    return my_letter

def menu():
    get_nums = True
    run = True
    while run is True:
        if get_nums is True:
            print("Lets get start and finish value")
            start = get_integer_input("Please enter start value: -> ")
            end = get_integer_input("Please enter start value: -> ")
            get_nums = False
        my_menu = '''
    A: Square
    B: Cube
    G: Get new numbers
    Q: Quit
                    '''
        print(my_menu)
        choice = get_string_input("Please choose an option: -> ")
        if choice == "A":
            square(start, end)
        elif choice == "B":
            cube(start, end)
        elif choice == "G":
            get_nums = True
        elif choice == "Q":
            run = False
            print("Thank you")
        else:
            print("you have not chose a valid option")


menu()