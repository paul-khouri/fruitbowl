"""Regular expressions checker"""
import re


pattern = "r'\d\d\d'"
s = "my 456number is 123"
t= "AS91058 jkakdhkshAS91067"

#match = re.search(r'[\d]+', s)
#match = re.findall(r'[\d]+', s)
#match = re.findall(r'[\d]+nu[mb]+', s)
match = re.findall(r'AS[0-9]{5,5}', t)
print(match)

pattern = '^[a-z-]{1,}$'
test_string = "AB3265727".lower()
test_match = re.search(pattern, test_string)
#print(test_match)


