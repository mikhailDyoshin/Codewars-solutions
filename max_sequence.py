def max_sequence(arr: list) -> int:

    """
        The function finds the maximum sum
        of a contiguous subsequence
        in an array or list of integers.
    """

    max_seq = 0
    curr_seq = 0
    for x in arr:
        curr_seq += x
        if curr_seq < 0:
            curr_seq = 0
        if curr_seq > max_seq:
            max_seq = curr_seq

    return max_seq 


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sequence(arr))