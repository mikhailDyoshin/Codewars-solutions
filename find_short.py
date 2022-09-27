def find_short(s: str) -> str:

    """
        The function takes a string of words
        and returns the length of the shortest word(s).
    """

    return min(len(x) for x in s.split())


s = "bitcoin take over the world maybe who knows perhaps"

print(find_short(s))