def dig_pow(n: int, p: int) -> int:

    """
        The function finds a positive integer k, if it exists, 
        such that the sum of the digits of n taken to the successive powers of p is equal to k * n

        In other words:
        Is there an integer k such as :
        (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

        If it is the case the function will return k, if not return -1

        Note: n and p should always be given as strictly positive integers.
    """

    s = 0
    for i,c in enumerate(str(n)):
        s += pow(int(c),p+i)
    return s/n if s%n==0 else -1