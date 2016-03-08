def payer(balance, interest, payment):
    remainingBalance = balance
    index = 1

    while index <= 12:
        temp = remainingBalance - payment
        remainingBalance = temp + temp * (interest / 12.0)
        index += 1

    return remainingBalance

def lowestPaymentFinder(balance, interest):
    payment = int(round(balance / 12.0, -1))
    remaining = payer(balance, interest, payment)

    while remaining > 0:
        payment += 10
        remaining = payer(balance, interest, payment)

    return payment
