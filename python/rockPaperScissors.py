import random

options = ["rock","paper","scissors"]
my_win = 0
computer_win = 0
print("Hello! You are inside rock paper scissores game!")
print("Type \"quit\" to stop the game at any moment!")
while True:
    playerInp = input("enter rock, paper or scissors: ").lower()
    computerInp = random.choice(options)

    if(playerInp=="quit"):
        break

    if(playerInp not in options):
        playerInp = input("your input is invalid try again: ")

    if playerInp == computerInp:
        print("Tie try again: ")
        print(f"you and computer both choose \"{computerInp}\"")
        continue

    elif(playerInp=="rock" and computerInp == "scissors") or (playerInp == "paper" and computerInp == "rock") or (playerInp =="scissors" and computerInp == "paper"):
        print(f"you choose \"{playerInp}\" and computer choose \"{computerInp}\"")
        print("You win!")
        my_win += 1
    
    else:
        print(f"you choose \"{playerInp}\" and computer choose \"{computerInp}\"")
        print("you lost!")
        computer_win += 1
print(f"game ended! your score {my_win} and computers score {computer_win}")