import random

print("Selecting a random number.")
randomNum = random.randint(1,101)
print("random number selected!")
gNum = int(input("Guess a number:"))
count =1
while gNum!= randomNum and count<7:
    count += 1
    print(f"you got {8-count} tries left")
    if(gNum>randomNum):
        gNum=int(input("You guessed high! Guess again:"))
    else:
        gNum=int(input("You guessed low! Guess again:"))
if gNum==randomNum:
    print("you guessed the right number!",gNum)
else :
    print("You couldnt guess the right word!")