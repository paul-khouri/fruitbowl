from difflib import SequenceMatcher

def get_string(m):
    return input(m)


def similar(a,b):
    return SequenceMatcher(None, a.lower(),b.lower()).ratio()

def check_string(f):
    new_fruit = get_string("Please enter new fruit: -> ")
    for x in f:
        r=similar(x, new_fruit)
        if r > 0.6:
            output = "Your entry of {} closely matches a prexisting entry of {}".format(new_fruit, x)
            print(output)
            choice = get_string("Enter y to use your entry or n to use the prexisting fruit (y/n): -> ")
            if choice == "y":
                print("Entry added")
            elif choice == "n":
                print("Reverting to update fruit function")
            else:
                print("unknown entry")





def main():
    fruit_set = ["mango", "pear", "plum", "pomegranate","rasberry","apple","apricot","blackberry"]
    a="abc"
    b=" cba"
    ratio= similar(a.lower(),b.lower())
    print(ratio)
    check_string(fruit_set)

main()