def update_light(current: str) -> str:

    """
        The function takes a string as an argument 
        representingthe current state of the light 
        and returns a string 
        representing the state the light should change to.

        For example, when the input is green, 
        output should be yellow.
    """

    if current == 'green':
        return 'yellow'
    elif current == 'yellow':
        return 'red'
    elif current == 'red':
        return 'green'