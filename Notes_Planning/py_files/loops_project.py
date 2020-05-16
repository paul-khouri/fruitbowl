
def get_integer(m):
    my_integer = int(input(m))
    return my_integer


def get_string(m):
    my_string = input(m)
    return my_string

def add_names_ages(N,A):
    num_entries = get_integer("How many names and ages would you like to add: -> ")
    c = 0
    while c < num_entries:
        name = get_string("Please enter name: -> " )
        age = get_integer("Please enter age: -> ")
        N.append(name)
        A.append(age)
        print("{} aged {} has been added".format(N[-1], A[-1]))
        c += 1
    print("All names added")

def review_lists(N,A):
    if len(N) == len(A):
        for i in range(0, len(N)):
            output = "{} {}".format(N[i], A[i])
            print(output)



def menu():
    names = []
    ages = []
    my_menu ='''
    A: Add names and ages
    B: Review 
    Q: Quit
    '''
    run = True
    while run == True:
        print(my_menu)
        option = get_string("Please choose option: -> ")
        if option == "A":
            add_names_ages(names, ages)
        elif option == "R":
            review_lists(names, ages)
        elif option == "Q":
            print("Thankyou")
            run = False
        else:
            print("Invalid entry")

menu()