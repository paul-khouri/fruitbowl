def get_string(m):
    my_string = input(m)
    return my_string

def get_integer(message):
    my_integer = int(input(message))
    return my_integer


def double_loop_print(L):
    for i in range(0, len(L)):
        output = "{} : {}".format(i, L[i])
        print(output)
        for j in range(0,len(L[i])):
            output = "{} : {}".format(j, L[i][j])
            print(output)

def single_loop_print(L):
    for i in range(0, len(L)):
        output = "{:10} ---   {:10}  ---  {:<10}".format(L[i][0], L[i][1], L[i][2] )
        print(output)

def print_with_indexes(L):
    for i in range(0, len(L)):
        output ="{:3} : {:10} {:10} {:10}".format(i,L[i][0], L[i][1], L[i][2])
        print(output)


def add_new_entry(L):
    print("Start adding new entry.")
    name = get_string("Please enter the new name: -> ")
    hair_colour = get_string("Please enter hair colour: -> ")
    age = get_integer("Please enter age: -> ")
    new_list = [name, hair_colour, age ]
    L.append(new_list)

def update_name(L):
    print_with_indexes(L)
    my_index = get_integer("Please enter the index number to update the name: -> ")
    new_name = get_string("Please enter the new name: -> ")
    old_name = L[my_index][0]
    L[my_index][0] = new_name
    output_message = "{} has now been changed to {}.".format(old_name , new_name)
    print(output_message)

def search(L):
    item = get_string("Please choose search item: -> ")
    # creating a variable ffound and initilise as false
    not_found = True
    for i in range(0, len(L)):
        for j in range(0,len(L[i])):
            if item == str(L[i][j]):
                print("Found it {} is at Row {} Column {}".format(item , i, j))
                print(L[i])
                # something has now be found so change to True
                not_found = False
    if not_found == True:
        print("Your item could not be found")









def main():
    my_L =[
        ["Alice", "Blond", 12],
        ["Cathy", "Blond", 15],
        ["Dan", "Black", 10],
        ["Bob", "Brown", 13],
        ["Joe", "Green", 13]
    ]
    #print(my_L)
    #double_loop_print(my_L)
    #single_loop_print(my_L)
    #print_with_indexes(my_L)
    #add_new_entry(my_L)

    #update_name(my_L)
    #print_with_indexes(my_L)
    search(my_L)






main()









def loop_with_indexes(L):
    for i in range(0, len(L)):
        output = "{:3} ->   {:10}   {:10}    {:<10}".format(i, L[i][0], L[i][1], L[i][2] )
        print(output)



def create_new_entry(L):
    name = get_string("Please enter name: -> ")
    hair_colour = get_string("Please enter hair colour: -> ")
    age = get_integer("Please enter age: -> ")
    L.append([name, hair_colour, age])
    return None




def update_name(L):
    loop_with_indexes(L)
    my_index = get_integer("Choose option number for name to update: -> ")
    new_name = get_string("Enter new name: -> ")
    old_name = L[my_index][0]
    L[my_index][0] = new_name
    my_string = "The name for {} has been updated to {}".format(old_name, new_name)
    print(my_string)
    return None

























