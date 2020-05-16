def square_num():
    for i in range(0,100):
        my_square = i*i
        my_output = "{} squared = {}".format(i, my_square)
        print(my_output)

#square_num()

def cube_num():
    for i in range(0,100):
        my_cube = i*i*i
        my_output = "{} cubed = {}".format(i, my_cube)
        print(my_output)
    print()


def get_integer():
    my_integer = int(input("Please enter number"))
    return my_integer


def menu():
    run = True
    while run == True:
        my_menu = '''
        A: Square
        B: Cube
        Q: Quit
        '''
        print(my_menu)
        choice = input("Please choose option")
        if choice == "A":
            square_num()
        elif choice == "B":
            cube_num()
        elif choice == "Q":
            run = False
            print("Thanks")
        else:
            print(" Invalid entry")

menu()