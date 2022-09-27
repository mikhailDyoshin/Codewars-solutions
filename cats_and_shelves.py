def cats_and_shelves(start: int, finish: int) -> int:

    """
        The function solves the task
        which described in cats_and_shelves.py 
    """
    
    distance = finish-start
    max_step = 3
    return sum(divmod(distance, max_step))


"""
    TASK:

    An infinite number of shelves
    are arranged one above the other in a staggered fashion.
    The cat can jump up to 3 shelves at the same time: 
    from shelf 1 to shelf 2 or 4 
    (the cat cannot climb on the shelf directly above its head).

    Find the minimum number of jumps to go from start to finish.
"""


print(cats_and_shelves(2, 4))