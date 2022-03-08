import random

choices = ["rock", "paper", "scissors"]

while True:
    computer = random.choice(choices)

    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    print("computer: " + computer)
    print("player: " + player)

    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!")
        elif computer == "scissors":
            print("You win!")
    elif player == "paper":
        if computer == "rock":
            print("You win!")
        elif computer == "scissors":
            print("You lose!")
    elif player == "scissors":
        if computer == "paper":
            print("You win!")
        elif computer == "rock":
            print("You lose!")

    play_again = input("Do you want to play again? y/n: ").lower()

    if play_again != "y":
        break
print("Bye!")
