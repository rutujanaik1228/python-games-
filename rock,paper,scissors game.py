import random

while True:
    p = input("Enter a choice (rock, paper, scissors): ")
    player=p.lower()
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    print("You chose",player)
    print("computer chose",computer)

    if player == computer:
        print(f"Both players selected {player}. It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player == "paper":
        if computer == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player  == "scissors":
        if computer == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    else:
        print("Invalid choice")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
    else:
        print("invalid choice")
