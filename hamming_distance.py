
def hamming_distance(a: str, b: str) -> int:

    """
        The function returns the hamming distance
         of the two strings as an integer.
    """

    return sum(x != y for x, y in zip(a, b))


a = '100101'
b = '101001'

print(hamming_distance(a, b))