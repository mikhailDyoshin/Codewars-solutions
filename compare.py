
def comp(array1: list, array2: list) -> bool:

    """
        The function checks 
        whether the two arrays have the "same" elements, 
        with the same multiplicities
        (the multiplicity of a member is the number of times it appears).
        "Same" means, here, that the elements in b are the elements in a squared,
        regardless of the order.

        EXAMPLES:

        Valid:
        a = [121, 144, 19, 161, 19, 144, 19, 11] 
        b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

        Invalid:
        a = [121, 144, 19, 161, 19, 144, 19, 11]  
        b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]

    """

    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False


array1 = [121, 144, 19, 161, 19, 144, 19, 11]
array2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

print(comp(array1, array2))
