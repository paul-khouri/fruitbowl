
def double_loop_print(L):
    for i in range(0, len(L)):
        output = "{} : {}".format(i, L[i])
        print(output)
        for j in range(0,len(L[i])):
            output = "{} : {}".format(j, L[i][j])
            print(output)


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
    for i in range(0, len(my_L)):
        output = "{:10} ---   {:10}  ---  {:<10}".format(my_L[i][0],my_L[i][1],my_L[i][2] )
        print(output)





main()































