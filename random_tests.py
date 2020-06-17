


from operator import itemgetter
L=[[0, 20, 'f'], [4, 2, 't'], [9, 4, 'afsd']]
L=sorted(L, key = lambda x: x[1])
#sorted(L, key=itemgetter(2))
print(L)

group_d = [
    {"Name": "Alice", "Hair": "Blond", "Age": 12},
    {"Name": "Bob", "Hair": "Brown", "Age": 13},
    {"Name": "Cathy", "Hair": "Blond", "Age": 15},
    {"Name": "Dan", "Hair": "Black", "Age": 10}
]

def loop_on_d(D):
    for x in D:
        my_string = "{:5} , {:5} , {:5}".format(x["Name"],x["Hair"], x["Age"] )
        print(my_string)
