import re

def one_():

    txt = "The rain in Spain"
    x = re.search("^The.*Spain$", txt)
    print(x)

    txt = "The rain in Spain"
    #string starting with The and ending with Spain
    x = re.search("^The.*Spain$", txt)

    if x:
        print(type(x))
        #print(x.match())
        print(x.span())

        print("YES! We have a match!")
    else:
        print("No match")

def two_():
    #Return a list containing every occurrence of "ai":
    txt = "The rain in Spain"
    x = re.findall("ai", txt)
    print(x)
    txt = "The rain in Spain"
    x = re.findall("^The.*Spain$", txt)
    print(x[0])

def three_():
    txt = "The rain in Spain"
    x = re.search("\s", txt)
    print(x)
    print("The first white-space character is located in position:", x.start())

def splitting():
    import re
    # Split the string at every white-space character:
    # \s is whitespace character
    txt = "The ra   in in S   pain"
    x = re.split("\s", txt)
    print(x)

def subbing():
    txt = "Hello I must be going"
    x = re.sub("o", "z", txt)
    print(x)
    x = re.sub("o", "z", txt,1)
    print(x)

def match_object():
    txt = "The Rain in Spain falls rarely on the Plains"
    # r is raw
    x = re.search(r"\bS\w+", txt)
    print(x)
    print(x.span())
    print(x.group())
    print(x.string)


def special_chars():
    txt = "The Rain in Spain falls rarely on the Plains"
    x=re.search("[a-m]+", txt)
    print(x)

    txt = "Achievement Standard AS90737 Do Something 4567"
    x = re.search("S[0-9]+", txt)
    x = re.search("7[0-9]+", txt)
    print(x)
    x = re.findall("[0-9]+", txt)
    print(x)


def email():
    txt ="harry@gmail.com"
    x=re.search(r"[a-zA-z0-9]+@+[a-zA-Z]+\.[a-z]+$",txt)
    print(x)
    x = re.search(r"\.[a-zA-Z]+", txt)
    print(x)

def phone():
    txt= "022507822"
    x=re.search(r"(^021)\d{6,8}|(^022)\d{6,8}|(^027)\d{6,8}", txt)
    print(x)
    txt = "02112345678"
    x = re.search(r"((^021)|(^022)|(^027))\d{6,7}", txt)
    print(x)

def getAllTextParts():
    temp = []
    txt="Atkinson, Aaliyah"
    x = re.findall(r"[a-zA-z]+", txt)
    temp = temp + x

    print(x)

    txt ="Upload File 139872734       1   11  Digital Technologies"
    x = re.findall(r"[a-zA-z0-9]+", txt)
    x.remove("Upload")
    x.remove("File")
    print(x)
    x = re.findall(r"[0-9]\d{1,8}", txt)
    print(x)
    temp = temp + x
    print(temp)
    x = re.findall(r"\b1\d{1}\s", txt)
    print(x)

def find_up_to_space():
    txt = "Atkinson, Aaliyah"
    x=re.findall(r"(.*) .*", txt)
    print(x)
    x = re.findall(r".* (.*)", txt)
    print(x)
    # all after a space
    x=re.findall(r"\s(.*)", txt)[0]
    print(x)

def find_key_name():
    txt = "Leeds Street Bake 18"
    x = re.findall(r"[a-zA-z0-9]+", txt)
    print(x)
    # if the length of the last digit is two, remove
    if x[-1].isdigit() and len(x[-1]) == 2:
        x.pop(-1)
    print(' '.join(x))
    txt ='4470Vodafone A'
    x = re.findall(r"[0-9]+[a-zA-z]+ ", txt)
    #result = ''.join([i for i in txt if not i.isdigit()])
    #print(result)
    txt=txt.lstrip('0123456789.- ')
    print(txt)





def split_test():
    txt = "Bhatnagar Stewart, Arushi"
    print(txt.split(","))

def regex_one():
    txt = "ABC123"
    x = re.findall(r"[A-Z]{3}\d{3}", txt)
    print(x)

def regex_two():
    txt = '4470Vodafone A'
    x = re.findall(r"^[0-9]+", txt)
    print(x)
    x = re.sub(x[0], "", txt)
    print(x)

def regex_three():
    txt = ' T WBC ATM'
    x = re.search(r"\sATM", txt)
    print(x)

def regex_four():
    txt = "ATM TRANSATMACTION ATM"
    x = re.findall(r"ATM\s|\sATM|^ATM", txt)
    print(x)
    txt ="ATM"
    x = re.findall(r"ATM\s|\sATM|^ATM", txt)
    print(x)

def regex_five():
    txt = '"First Name"'
    print(txt)
    txt = re.sub('"', '', txt)
    print(txt)






#two_()
#splitting()
#subbing()
#match_object()
#special_chars()
#email()
#phone()
#getAllTextParts()
#split_test()
#find_up_to_space()
#find_key_name()
#regex_one()
#regex_two()
#regex_three()
#regex_four()
regex_five()
