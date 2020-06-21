def get_validated_integer(m, min, max):
    """to ensure a valid integer is returned
        tests for inclusive minimum and maximum
        3 arguments string message int min int max
    """
    while True:
        try:
            my_int = int(input(m))
        except ValueError:
            print("This is not a valid entry. A whole number is needed")
            continue
        if my_int < min:
            print("Your entry value is too small")
        elif my_int > max:
            print("Your entry value is too large")
        else:
            return my_int









if __name__ == "__main__":
    test_num = get_validated_integer("Please enter your number: -> ", 0, 5)
    print(test_num)








