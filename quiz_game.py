print("lets play computer game!")

playing = input("Do you want to play computer game? ")

if playing != "yes":
    quit()

print("lets play!!")
grade = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("correct")
    grade +=1
else:
    print("Incorrect")

answer = input("What does MP stands for? ")
if answer.lower() == "member of parliament":
    print("correct")
    grade +=1
else:
    print("Incorrect")

answer = input("What does GV stands for? ")
if answer.lower() == "government":
    print("correct")
    grade +=1
else:
    print("Incorrect")

answer = input("What does EU stands for? ")
if answer.lower() == "european union":
    print("correct")
    grade +=1
else:
    print("Incorrect")

print(grade)