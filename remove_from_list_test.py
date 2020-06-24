fruit_bowl=[
    ["apples", 0],
    ["pears",0],
    ["quinces", 7],
    ["lemons", 0]
]


def remove_zeros(f):
    i = 0
    while i < len(f):
        if f[i][1] == 0:
            f.pop(i)
            i -= 1
        i += 1




remove_zeros(fruit_bowl)
print(fruit_bowl)
