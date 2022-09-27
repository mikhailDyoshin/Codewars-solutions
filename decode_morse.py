def decode_morse(s: str) -> str:

    """
        The function takes the morse code as input
        and return a decoded human-readable string.
    """

    # Strip spaces around the message
    s_striped = s.strip()

    # Split message into words
    words = s_striped.split('   ')

    # Split each word into letters
    l = []
    for word in words:
        simbols = word.split()
        l.append(simbols)
    
    # Decode each letter and add them to lists which represent words
    message_decode = []
    for word in l:
        word_decode = []
        for simb in word:
            word_decode.append(MORSE_CODE[simb])
        message_decode.append(word_decode)
    
    # Form decoded words
    words_decode = []
    for simbols in message_decode:
        word = ''.join(simbols)
        words_decode.append(word)

    # Form decoded message 
    message = ' '.join(words_decode)   
    
    return message

s = '.... . -.--   .--- ..- -.. .'

print(decode_morse(s))
