def annualInvoice(balance, interestRate, paymentRate):
    remainingBalance = balance
    index = 1
    totalPaid = 0

    while index <= 12:
        payment = paymentRate * remainingBalance

        print("Month: " + str(index))
        print("Minimum monthly payment: " + str(round(payment, 2)))

        preinterest = remainingBalance - payment
        totalPaid += remainingBalance - preinterest
        remainingBalance = preinterest + preinterest * (interestRate / 12.0)

        print("Remaining balance: " + str(round(remainingBalance, 2)))

        index += 1
    
    print("Total paid: " + str(round(totalPaid, 2)))
    print("Remaining balance: " + str(round(remainingBalance, 2)))
