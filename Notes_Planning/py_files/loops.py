def while_loop_counter(count):
    # requires a counter
    c = 0
    # condition is set on the counter value
    while c < count:
        print("hello")
        # counter must be incremented
        c +=1
    print("All done")


def while_loop_indefinite():
    # set a condition
    run = True
    # check the condition
    while run is True:
        choice = input("Enter Q to quit or any other key to stay where you are: -> ")
        if choice == "Q":
            print("See you later")
            run = False
        else:
            print("I am still here")


def for_in_range_loop():
    # this has a built in counter
    # can be anything but we generally use i or j or k
    # can add steps
    for i in range(6,50, 3):
        print(i)


def double_loop():
    for i in range(0,10):
        for j in range(0,10):
            print(" ({:^2}, {:^2})".format(j,i), end="")
        print()


def menu():
    my_menu = '''
                1: while loop with counter
                2: while loop with quit
                3: for in range
                4: double loop
                0: quit
                '''
    print(my_menu)
    choice = int(input("choose your option: -> "))
    if choice is 1:
        amount = int(input("How many would you like: -> "))
        while_loop_counter(amount)
    elif choice is 2:
        while_loop_indefinite()
    elif choice is 3:
        for_in_range_loop()
    elif choice is 4:
        double_loop()
    elif choice is 5:
        print("Thank you")


menu()