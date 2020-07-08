"""Regular expressions checker"""
import re


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


