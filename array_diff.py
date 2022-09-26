def array_diff(a: list, b: list) -> list:
    """
        A difference function, 
        which subtracts one list from another 
        and returns the result.
        
        It removes all values from list 'a', 
        which are present in list 'b' keeping their order.
        
        If a value is present in 'b',
        all of its occurrences 
        will be removed from the other list.
    """
    return [x for x in a if x not in b]


a = [1, 1, 1, 2, 1]
b = [1, 0]

print(array_diff(a, b))