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


while True:
    guess_number = input("Guess a number")
    if guess_number.isdigit():
        guess_number = int(guess_number)
    
    else:
        print("Kindly enter integer!!")
        quit()
    if guess_number == random_no:
        print("You got it!!")
        break
    else:
        print("You got it wrong")
