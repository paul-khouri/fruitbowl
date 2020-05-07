
def print_list(L):
    my_string = ""
    counter = 0
    for x in L:
        if counter == len(L)-1:
            my_string =  my_string + str(x)
        else:
            my_string = my_string + str(x) + " , "

        counter += 1
    print(my_string)

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

def add_nums(L):
    sum = 0
    for x in L:
        sum += x
    return sum

def product_nums(L):
    product = 1
    for x in L:
        product = product*x
    return product

def average_nums(L):
    sum = add_nums(L)
    average = sum/len(L)
    return average


final_list = get_numbers()
final_sum = add_nums(final_list)
print(final_sum)
final_product = product_nums(final_list)
print(final_product)
final_average = average_nums(final_list)
print(final_average)





