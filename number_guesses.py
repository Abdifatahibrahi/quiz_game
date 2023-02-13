import random

top_of_range = input("Type a number: ")



if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Kindly enter an integer that is greater than 0")
        quit()
else:
    print("Kindly enter integer!!")
    quit()

random_no = random.randint(0,top_of_range)

guesses = 0


while True:
    guess_number = input("Guess a number: ")
    guesses += 1
    if guess_number.isdigit():
        guess_number = int(guess_number)
    
    else:
        print("Kindly enter integer!!")
        continue
    if guess_number == random_no:
        print("You got it!!")
        break
    else:
        if guess_number > random_no:
            print("You are above the number")
        else: 
            print("You are below the number")

if guesses > 1:
    print("You got it in", guesses, "guesses")
else:  
    print("You got it in", guesses, "guess")    