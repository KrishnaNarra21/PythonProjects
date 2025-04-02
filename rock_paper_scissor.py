import random

user_wins = 0
system_wins = 0

choose = ["rock", "paper", "scissor"]

while True:
    user_pick = input("Pick your choice Rock/Paper/Scissor or q to quit this game: ").lower()

    if user_pick == "q":
        break

    if user_pick not in choose:
        print("wrong choose, next time choose right one")
        continue

    random_pick = random.randint(0,2)
    system_pick = choose[random_pick]

    if (user_pick == "rock" and system_pick == "scissor") or \
        (user_pick == "scissor" and system_pick == "paper") or \
        (user_pick == "paper" and system_pick == "scissor"):
        print("Great, You Won!")
        user_wins += 1

    elif user_pick == system_pick:
        print("Ohh! It's a tie.")

    else:
        print("Sorry, System Won!")
        system_wins += 1

print("You win",user_wins,"times")
print("System win",system_wins,"times")

if user_wins > system_wins:
    print("Congrats, you are a winner")
elif user_wins < system_wins:
    print("So, this time system is winner")
else:
    print("Its a tie")

print("GoodBye, Take Care!")


"""
This Python script is a Rock, Paper, Scissors game where the user plays against the system.
The user selects an option, and the system randomly picks one. 
The game follows standard rules: Rock beats Scissors, Scissors beats Paper, and Paper beats Rock. 
Wins are tracked, and after exiting, the final winner is announced.
"""