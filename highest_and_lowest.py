def high_and_low(s: str) -> str:

    """
        The function takes a string of space separated numbers, 
        and returns the highest and lowest number.
    """

    s_list = [int(x) for x in s.split()]
    high = str(max(s_list))
    low = str(min(s_list))
    out = ' '.join([high, low])
    return out


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))