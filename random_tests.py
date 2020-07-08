


from operator import itemgetter
L=[[0, 20, 'f'], [4, 2, 't'], [9, 4, 'afsd']]
L=sorted(L, key = lambda x: x[1])
#sorted(L, key=itemgetter(2))
#print(L)

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


def test_prices_tuple():
    regular_price = 16.5
    gourmet_price = regular_price + 7
    map=("name", "price", "description")
    pizzas=[
        ("Supreme", regular_price, "All our best toppings in one place"),
        ("Vegetarian", gourmet_price, "Our meat free zone"),
        ("Hawaiian", gourmet_price, "Our meat free zone")
    ]

    sum_row_column_list(pizzas,1)


def sum_row_column_list(l,i):
    """Print one column of a row column list

    :param l: list (2D)
    :param i: int (column index#)
    :return: None
    """

    for j in range(0, len(l)):
        output = "{}".format(l[j][i])
        print(output)



test_prices_tuple()
