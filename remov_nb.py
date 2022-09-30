def remov_nb(n: int) -> list:

    """
        This function solves the task below.

        TASK:
        - A friend of mine takes the sequence of all numbers
        from 1 to n (where n > 0).
        - Within that sequence, he chooses two numbers, a and b.
        - He says that the product of a and b
        should be equal to the sum of all numbers in the sequence,
        excluding a and b.
        - Given a number n, could you tell me the numbers
        he excluded from the sequence?

        The function takes the parameter n
        (n is always strictly greater than 0)
        and returns a list of the form: [(a, b), ...]
        with all (a, b) which are the possible removed numbers
        in the sequence 1 to n.
    """

    l = [x for x in range(1, n+1)]

    S = n*(n+1)/2
    result = []               
    for a in l:
        sol = (S - a)%(a+1)
        b = (S - a)/(a+1)
        if sol == 0 and 1<b<n+1:
            result.append((a, int(b)))

    return result

n = 101
print(remov_nb(n))