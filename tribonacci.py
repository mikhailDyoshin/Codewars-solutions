def tribonacci(signature: list, n: int) -> list:

    """
        This function is a fibonacci function
        that given a signature array/list,
        returns the first n elements - signature included -
        of the so seeded sequence.
    """

    numbers = signature
    if n <= 3:
        return [numbers[i] for i in range(n)]
    else:
        for i in range(n-3):
            next = sum(numbers[i:i+3])
            numbers.append(next)
        return numbers

print(tribonacci([1, 1, 1], 4))