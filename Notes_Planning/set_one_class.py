

def go_print():
     print("Hello my name is Jane")

def go_print_var():
     name = "Melissa"
     age = 8
     my_string = "My name is {} \nI am {} years old".format(name, age)
     print(my_string)

def go_print_args(n,a):
     name = n
     age = a
     my_string = "My name is {} \nI am {} years old".format(name, age)
     print(my_string)

def get_integer_input():
     my_input = int(input("Please enter a number: -> "))
     # the function terminates when a return is called
     return my_input


def menu():
     my_menu = '''
     1 : go print
     2 : go print var
     3 : go print args
     0 : quit
     '''
     print(my_menu)
     user_choice = get_integer_input()
     if user_choice == 1:
          go_print()
     elif user_choice == 2:
          go_print_var()
     elif user_choice == 3:
          go_print_args("Jessie", 5)
     elif user_choice == 0:
          print("Thankyou")
     else:
          print("Unrecognised entry")

menu()
     



