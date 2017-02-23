numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

import random
number = random.choice(numbers)
for i in range(1, 6):

    guess = raw_input("Guess a number between 1 and 20: ")
    guess = int(guess)

    if guess == number:
        print "Great job! you win"
        break
    elif guess > 20 or guess < 1:
        print "Oops, that number is not in 1 through 20!"
    else:
        print "That is not correct."

print "The correct answer was %d." % number
print "All done."
