# loops
# loops are repeated actions (iterations)


# loop with a counter (will run a certain number of times)
def loop_with_counter():
    c = 0
    while c < 10:
        print(   "hello c is now {}".format(c)    )
        # increment c
        c += 1
    return None

# indefinite loop
def indefinite_loop():
    run = True
    while run == True:
        user_choice = input("Press 'n' to stop the loop \n or anything else to stay in it: -> ")
        if user_choice == "n":
            print("Loop will stop")
            run = False
        else:
            print("You are still in the loop")


def for_in_range_loop():
    # this has a built in counter
    # can be anything but we generally use i or j or k
    # can add steps
    for i in range(3, 20):
        print(i)

# double loop
def double_loop():
    for i in range(0,5):
        for j in range(0,6):
            print( "({} , {}) ".format(j,i) , end = "" )
        print()



# loop_with_counter()
# indefinite_loop()
# for_in_range_loop()
double_loop()

