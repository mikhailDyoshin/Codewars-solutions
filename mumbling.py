def accum(s: str) -> str:

    """
        There is an example how this function works:

        accum("abcd") -> "A-Bb-Ccc-Dddd"

        accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"

        accum("cwAt") -> "C-Ww-Aaa-Tttt"
    """

    letters = [let for let in s]

    words = []
    i = 1
    for letter in letters:
        word = letter.upper() + letter.lower()*(i-1)
        words.append(word)
        i += 1

    out = '-'.join(words)

    return out


s = 'ZpglnRxqenU'
print(accum(s))