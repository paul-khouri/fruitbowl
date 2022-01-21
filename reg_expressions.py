"""Regular expressions checker"""
import re

def test_one():
    pattern = "r'\d\d\d'"
    s = "my 456number is 123"
    t= "AS910586758 jkakdhkshAS91067"

    #match = re.search(r'[\d]+', s)
    #match = re.findall(r'[\d]+', s)
    #match = re.findall(r'[\d]+nu[mb]+', s)
    match = re.findall(r'AS[0-9]{5,5}', t)
    #print(match)

    # at least one character all a,..,z or -
    pattern = '^[a-z-]{1,}$'

    test_string = "paul56ll".lower()
    test_match = re.search(pattern, test_string)
    print(test_match)

def test_two():
    while True:
        user_input = input("Enter phone")


        x = re.search(
            "(^\([0][3]\))(\d{7}$)|(^\([0][4]\))(\d{7}$)|"
            "(^\([0][6]\))(\d{7}$)|(^\([0][7]\))(\d{7}$)|"
            "(^\([0][9]\))(\d{7}$)|(^\([0][2][1]\))(\d{6,8}$)|"
            "(^\([0][2][2]\))(\d{6,8}$)|(^\([0][2][7]\))(\d{6,8}$)|"
            "(^\([0][2][9]\))(\d{6,8}$)|([0][8][0][0])([\s])(\d{5,8}$)",
            user_input)

        print(x)

        if x:
            return user_input
        else:
            print("Sorry your phone number was not at match")



test_two()


