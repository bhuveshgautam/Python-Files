low = 0
high = 100
guess = (low + high) / 2

ans = ""

print("Please think of a number between 0 and 100!")
while ans != "c":
    print("Is your secret number " + str(guess) + "?")
    ans = raw_input("Enter 'l' for too low, 'h' for too high, or 'c' for correct: ")
    while ans != 'l' and ans != 'h' and ans != 'c':
        print("Sorry, I did not understand your input.")
        print("Is your secret number " + str(guess) + "?")
        ans = raw_input("Enter 'l' for too low, 'h' for too high, or 'c' for correct: ")

    if ans == 'l':
        low = guess
        guess = (guess + high) / 2
    elif ans == 'h':
        high = guess
        guess = (low + guess) / 2

print("Game over. Your secret number was: " + str(guess))
