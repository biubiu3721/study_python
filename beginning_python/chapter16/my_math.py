def square(x):
    """
    calc square and return result
    :param x:
    :return:
    """
    return x * x


def prod(x, y):
    if x == 7 and y == 9:
        return x * y
       # return "An insidious bu has surfaced!"
    else:
        return x * y


if __name__ == "__main__":
    import doctest, my_math
    doctest.testmod(my_math)