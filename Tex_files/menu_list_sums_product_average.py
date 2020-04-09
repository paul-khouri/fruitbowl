def get_numbers():
    num_list = []
    counter = 0
    while counter < 3:
        num = int(input("Please enter a number "))
        num_list.append(num)
        counter += 1
    num_list.sort()
    print_list(num_list)
    return num_list


def print_list(l):
    my_string = ""
    counter = 0
    for x in l:
        if counter == len(l) - 1:
            my_string = my_string + str(x)
        else:
            my_string = my_string + str(x) + " , "

        counter += 1
    print(my_string)


def add_nums(l):
    _sum = 0
    for x in l:
        _sum += x
    return _sum


def product_nums(l):
    product = 1
    for x in l:
        product = product * x
    return product


def average_nums(l):
    _sum = add_nums(l)
    average = _sum / len(l)
    return average


def print_output(m, v):
    print(30 * "-")
    print("Your {} is :  {}".format(m, v))
    print(30 * "-")


def run_menu():
    menu = True
    menu_list = ["Enter set", "Get average", "Get sum", "Get product"]
    set = []
    while menu is True:
        for i in range(0, len(menu_list)):
            print("{:<5}{:^10} {:20}".format(i, "--", menu_list[i]))
        user_choice = input("Please choose your option:  ")
        if user_choice == "q":
            return
        else:
            user_choice = int(user_choice)
        if user_choice != 0 and len(set) == 0:
            print("You have an empty set")
            continue
        if user_choice == 0:
            set = get_numbers()
        elif user_choice == 1:
            average = average_nums(set)
            print_output("average", average)
        elif user_choice == 2:
            sum = add_nums(set)
            print_output("sum", sum)
        elif user_choice == 3:
            product = product_nums(set)
            print_output("product", product)
        else:
            print("Unrecognised entry")


if __name__ == "__main__":
    run_menu()
