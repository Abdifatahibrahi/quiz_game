question = input("Do you want to play game? ")

if question != "yes":
    quit()
print("Ok, let's play")

answer = input("What does CPU stands for? ")
if answer == "central processing unit":
    print('Correct')
answer = input("What does MP stands for? ")
if answer == "member of parliament":
    print('Correct')
answer = input("What does GV stands for? ")
if answer == "Government":
    print('Correct')

