amy_fruit_bowl = [
        ["Apples", 5],
        ["Pears", 7],
        ["Mangoes", 2],
        ["Kiwi Fruit", 9],
        ["Peasches", 3]
        ]

def add_fruit(L):
    """print list with item numbers
      get user quantity and add to list
      Argument:
      L -- 2 dimensional list  m x [string, integer]
      """
    header ="{:^12}{:30}{:2}".format("Item #", "Fruit", "Quantity")
    print(header)
    for i in range(0,len(L)):
        row = "{:^12}{:30}{:2}".format(i, L[i][0], L[i][1])
        print(row)
    message = "Please choose an item number to add fruit to?   "
    # must have full integer validation
    user_choice = int(input(message))
    message = "How many {} would you like to add?   ".format(L[user_choice][0])
    user_number = int(input(message))
    L[user_choice][1] += user_number
    confirmation_message = "You now have {} {} in the fruit bowl".format(L[user_choice][1], L[user_choice][0])
    print(confirmation_message)


add_fruit(amy_fruit_bowl)