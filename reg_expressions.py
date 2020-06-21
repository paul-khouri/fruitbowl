"""Regular expressions checker"""
import re


pattern = "r'\d\d\d'"
s = "my 456number is 123"
t= "AS91058"

#match = re.search(r'[\d]+', s)
#match = re.findall(r'[\d]+', s)
#match = re.findall(r'[\d]+nu[mb]+', s)
match = re.findall(r'AS[0-9]{5,5}', t)
print(match)

