def range_loop():
    for i in range(0,2*10, 1):
        print(i/2)
    return None

def range_powers():
    for i in range(0,10):
        my_value = "{:<7}  {:<7}  {:<7}".format(i, i*i , i*i*i)
        print(my_value)

def fib_sequence():
    m=1
    n=1
    while n<100000000000:
        f_sum = m+n
        m=n
        n=f_sum
        print(n)
        print(n/m)
fib_sequence()

#range_powers()