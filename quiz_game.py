"""
The program greets the user and asks if they want to play.
If the user does not enter "yes", the program quits.
If they enter "yes", the quiz starts.
The quiz consists of 5 multiple-choice questions about computer hardware.
Each correct answer increases the score by 1.
At the end, the program displays the user's score and their percentage of correct answers.
"""


print("Hello, Welcome to the computer quiz!")

yn = input("do have interest to play? ")

if yn != "yes".lower():
    quit()

print("let's start quiz")
score = 0

_1st = input("1) what does CPU stands for? ").lower()
if _1st == "central processing unit":
    print("Great, You are Correct!")
    score += 1
else:
    print("Sorry, Wrong Answer!")

_2nd = input("2) what does HDMI stands for? ").lower()
if _2nd == "high definition multimedia interface":
    print("Great, You are Correct!")
    score += 1
else:
    print("Sorry, Wrong Answer!")

_3rd = input("3) what does SSD stands for? ").lower()
if _3rd == "solid state drive":
    print("Great, You are Correct!")
    score += 1
else:
    print("Sorry, Wrong Answer!")

_4th = input("4) what does RAM stands for? ").lower()
if _4th == "random access memory":
    print("Great, You are Correct!")
    score += 1
else:
    print("Sorry, Wrong Answer!")

_5th = input("5) what does GPU stands for? ").lower()
if _5th == "graphics processing unit":
    print("Great, You are Correct!")
    score += 1
else:
    print("Sorry, Wrong Answer!")

print(f"your score is '{score}' correct out of '5' questions")
print(f"you got in {(score/5)*100}% in this quiz")



