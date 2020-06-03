class FruitBowl:
    # static variable
    __private_var = 20

    def __init__(self, name):
        self.name = name
        self.fruit = []

    def add_list_fruit(self, L):
        if len(self.fruit) == 0:
            self.fruit = L
        else:
            print("There is already fruit in the bowl")

    def add_to_fruit(self):
        self.__print_with_indexes()
        choice = int(input("Please choose fruit to add to: -> "))
        q_string = "How many {} would you like to add? -> ".format(self.fruit[choice][0])
        quantity = int(input(q_string))
        self.fruit[choice][1] += quantity

    def __print_with_indexes(self):
        for i in range(0, len(self.fruit)):
            row = "{} : ".format(i)
            for j in range(0, len(self.fruit[i])):
                row += "{:<15}".format(self.fruit[i][j])
            print(row)

    def review(self):
        for i in range(0, len(self.fruit)):
            row = ""
            for j in range(0, len(self.fruit[i])):
                row += "{:<15}".format(self.fruit[i][j])
            print(row)



def main():
    base_set =[
        ["apples", 0],
        ["pears", 0],
        ["quinces", 0],
        ["lemons", 0]
    ]
    f = FruitBowl("Jane")
    f.add_list_fruit(base_set)
    f.review()
    f.add_to_fruit()
    f.review()

main()

