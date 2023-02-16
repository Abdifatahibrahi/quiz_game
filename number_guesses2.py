import random

top_random = input("Enter the maximum number of your range: ")

if top_random.isdigit():
    top_random = int(top_random)
    if top_random <= 0:
        print("Enter a number greater than 0")
        quit()
else:
    print("Enter an interger ")
    quit()

random_number = random.randint(1, top_random)
guess = 0

while True:
    guess_number = input("Guess a number: ")
    guess += 1
    if guess_number.isdigit():
        guess_number = int(guess_number)
        if guess_number == random_number:
            print("You got it correct!")
            break
        elif guess_number > random_number:
            print("Your guess number is greater than your random number")
            continue
        elif guess_number < random_number:
            print("Your guess number is less than your random number")
            continue

    else:
        print("Enter an interger ")
        quit()

if guess > 1:
    print("You got in", guess, "guesses")
else:
    print("You got in", guess, "guess")