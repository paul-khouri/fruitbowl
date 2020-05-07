fruit_list = [
["Apples", 5],
["Pears", 7],
["Mangoes", 2],
["Kiwi Fruit", 9],
["Peaches", 3]
]

def print_contents(list):
    for x in list:
        out_string="{:15} - {:>10}".format(x[0], x[1])
        print(out_string)

print("R : Review Contents")
print("Q : Quit")
user_option = input("Please choose your options: ->   ")
if user_option == "R":
    print_contents(fruit_list)
