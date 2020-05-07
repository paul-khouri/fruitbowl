

def go_print():
     print("Hello my name is Jane")

def go_print_var():
     name = "Bob"
     age = 10
     # put them together in a string
     my_string = "My name is {} \nI am {} years old".format(name, age)
     print(my_string)

def go_print_args(n,a):
     name = n
     age = a
     my_string = "My name is {} \nI am {} years old".format(name, age)
     print(my_string)

def get_integer_input():
     my_number = int(input("please enter number: -> "))
     return my_number

def menu():
     run = True
     while run is True:
          my_menu = '''
                    1: go print
                    2: go print var
                    3: go print args
                    0: quit
                    '''
          print(my_menu)
          choice = get_integer_input()
          if choice == 1:
               go_print()
          elif choice == 2:
               go_print_var()
          elif choice == 3:
               go_print_args("Jill", 0)
          elif choice == 0:
               run = False
               print("Thank you")
          else:
               print("you have not chose a valid option")
          
menu()
