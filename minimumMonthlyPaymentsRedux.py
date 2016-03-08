def payer(balance, interest, payment):
    """
    balance: int or float > 0.0
    interest: float < 1.0
    payment: int or float > 0.0

    Calculates the remainder of balance after a year
    of monthly payments at payment and an interest
    rate of interest.
    """
    
    remainder = balance
    

    for _ in range(1, 13):
        temp = remainder - payment
        remainder = temp + temp * (interest / 12.0)

    return remainder

def paymentFinder(balance, interest):
    """
    balance: int or float > 0.0
    interest: float

    Finds the minimum montly payment on balance
    with an interest rate of interest over a
    twelve month period.
    """

    low = balance / 12
    high = (balance * ((1 + (interest / 12.0)) ** 12.0)) / 12.0
    payment = (low + high) / 2
    remainder = payer(balance, interest, payment)

    while remainder > 0 or 0 - remainder > 0.001:
        if remainder > 0:
            low = payment
        else:
            high = payment

        payment = (low + high) / 2
        remainder = payer(balance, interest, payment)

    return round(payment, 2)
