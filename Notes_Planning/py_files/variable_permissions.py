def update_var(v):
    v = 8
    return None


def add_in_list(L, M):
    for x in M:
        L.append(x)


def update_list(L):
    L.append("Bill")
    del L[1]
    print(id(L))
    L[1] = "Dan"
    print(id(L))
    add_in_list(L,["Mike", "Bob"])
    L.sort()
    return None


def menu():
    n = 1
    v = n
    print(id(n))
    print(id(v))
    v = 2
    print(id(v))
    my_list=["A","B","C"]
    my_list = my_list + ["Sue", "Gretal"]
    print(n)
    update_list(my_list)
    print(my_list)
    print(id(my_list))

    return None

menu()