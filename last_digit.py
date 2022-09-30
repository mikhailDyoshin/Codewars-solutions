def last_digit(n1: int, n2: int) -> int:

    """
        The function finds the last digit
        of the n1^n2
    """

    # First, check if the power is zero
    if n2 == 0:
        return 1
    
    # Find the last digit of the n1
    ld1 = n1%10

    # Form the multiplicative period
    period = [ld1**x%10 for x in range(1, 4)]
    period.insert(0, ld1**4%10)

    # The last digit of the n1^n2
    result = period[n2%4]

    return result


n1 = 9
n2 = 7
print(last_digit(n1, n2))