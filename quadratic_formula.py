def quadratic_formula(a: float, b: float, c: float) -> list:
    
    """
        The function takes three arguments, a, b, and c 
        that represent the coefficients in a formula
        of the form ax^2 + bx + c = 0.

        The function returns a list with two elements 
        where each element is one of the two roots.

        If the formula produces a double root
        the result should be a list
        where both elements are that value.
    """

    root1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    
    root2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    
    return [root1, root2]


print(quadratic_formula(2, 16, 1))
