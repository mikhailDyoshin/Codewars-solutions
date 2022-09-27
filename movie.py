import math

def movie(card: float, ticket: float, perc: float) -> int:

    """
        The function movie has 3 parameters: 
        card (price of the card), 
        ticket (normal price of a ticket), 
        perc (fraction of what he paid for the previous ticket) 
        and returns the first n such that
        ceil(price of System B) < price of System A.
    """

    priceA = 0
    priceB = card
    times = 0
    ticket_new = ticket
    while math.ceil(priceB) >= round(priceA):
        ticket_new *= perc
        priceA += ticket
        priceB += ticket_new
        times += 1
    else:
        return times

"""
    TASK:
    My friend John likes to go to the cinema. 
    He can choose between system A and system B.

    System A : he buys a ticket (15 dollars) every time
    System B : he buys a card (500 dollars) and a first ticket 
    for 0.90 times the ticket price, 
    then for each additional ticket 
    he pays 0.90 times the price paid for the previous ticket.

    John wants to know how many times he must go to the cinema
    so that the final result of System B, 
    when rounded up to the next dollar, 
    will be cheaper than System A.
"""

print(movie(100, 10, 0.95))