def get_integer(m):
    my_integer = int(input(m))
    return my_integer


def get_string(m):
    my_string = input(m)
    return my_string


def add_name_age(N, A):
    count = get_integer("How many names and ages  would you like to add? -> ")
    for i in range(0, count):
        name = get_string("Please enter name: - > ")
        age = get_integer("Please enter age: -> ")
        N.append(name)
        A.append(age)


def review(N, A):
    if len(A) == len(N):
        for i in range(0, len(A)):
            output = "{} is {} years old".format(N[i],A[i])
            print(output)






def menu():
    name=[]
    age=[]
    my_menu='''
    A: Add names and ages
    R: Review
    Q: Quit
    '''
    run = True
    while run == True:
        choice = get_string("Please enter choice: -> ")
        if choice == "A":
            add_name_age(name, age)
        elif choice == "R":
            review(name,age)



menu()