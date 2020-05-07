def add(a,b):
    my_result = a + b
    my_string = "{} + {} = {}".format(a, b, my_result)
    return my_string

def subtract(a,b):
    my_result = a - b
    my_string = "{} - {} = {}".format(a, b, my_result)
    return my_string

def multiply(a,b):
    my_result = a* b
    my_string = "{} * {} = {}".format(a, b, my_result)
    return my_string

def divide(a,b):
    my_result = a / b
    my_string = "{} / {} = {}".format(a, b, my_result)
    return my_string


def get_integer_input():
    my_number = int(input("please enter number: -> "))
    return my_number


def menu():
    get_nums = True
    run = True
    while run is True:
        if get_nums is True:
            print("Lets get two numbers")
            num_one = get_integer_input()
            num_two = get_integer_input()
            get_nums = False
        my_menu = '''
                    1: add
                    2: subtract
                    3: multiply
                    4: divide
                    5: get new numbers
                    0: quit
                    '''
        print(my_menu)
        choice = get_integer_input()
        if choice == 1:
            result = add(num_one, num_two)
        elif choice == 2:
            result = subtract(num_one, num_two)
        elif choice == 3:
            result = multiply(num_one, num_two)
        elif choice == 4:
            result = divide(num_one, num_two)
        elif choice == 5:
            get_nums = True
        elif choice == 0:
            run = False
            print("Thank you")
        else:
            print("you have not chose a valid option")
        if choice in [1,2,3,4]:
            print(result)


menu()