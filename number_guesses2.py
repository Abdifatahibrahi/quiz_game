import random

top_of_range = input("Enter the top of your range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Kindly enter a number that is greater than 0")
        quit()
else:
    print("Enter a digit next time!!")
    quit()

random_no = random.randint(0,top_of_range)
guesses = 0

while True:
    guess_no = input("Guess a number: ")
    guesses += 1
    if guess_no.isdigit():
        guess_no = int(guess_no)
    
    else:
        print("Enter a digit next time!!")
        continue
    if guess_no == random_no:
        print("You got it correct")
        break
    elif guess_no > random_no:
        print("Your guess number is above the random number")
    else:
        print("Your guess number is below the random number")


print("You got it in", guesses, "guesses")