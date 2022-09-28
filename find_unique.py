
def find_uniq(arr: list) -> float:

    """
        The functions takes an array with some numbers.
        All numbers are equal except for one.
        Function returns this number.
    """

    a, b = set(arr)

    if arr.count(a) == 1:
        return a
    else:
        return b


l = [ 1, 1, 1, 2, 1, 1 ]
print(find_uniq(l))
