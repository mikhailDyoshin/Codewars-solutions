def move_zeros(lst: list) -> list:

    """
        The function takes an array
        and moves all of the zeros to the end,
        preserving the order of the other elements.
    """

    new_lst = sorted(lst, key=lambda x: x==0 and type(x) is not bool)
    return new_lst


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
