#Hand Cricket Game
from random import choice

print("---------------------------------")
print("")
print("Welcome to the hand cricket game.")
print("")
print("---------------------------------")

coin = ["Heads","Tails"]
runs=[1,2,3,4,6]
playerOneScore = 0
playerTwoScore = 0 
count=0

#-------------------------------------------------------------

def coinToss(headsOrTails):
    flip = choice(coin)
    if(flip==headsOrTails):
        print("Player 1 won the toss!")
        print("")
        print("-----------------------------------")
    else:
        print("Player 2 won the toss!")
        print("")
        print("-----------------------------------")


def swapBatOrBall(batOrBall):
    if(batOrBall=="Bat"):
        return "Ball"
    return "Bat"

#--------------------------------------------------------------
print("")
overs = int(input("How many overs would you like to play?: "))
print("")

print("-----------------------------------")
print("")
headsOrTails = input("Do you call Heads or Tails?: ")
print("")
coinToss(headsOrTails)

print("")
batOrBall = input("Would you like to Bat or Ball?: ")
print("")

if(batOrBall=="Bat"):
    print("You are batting first.")
    print("")
    print("-----------------------------------")
elif(batOrBall=="Ball"):
    print("You are bowling first.")
    print("")
    print("-----------------------------------")



while(count<overs*6):
    if(batOrBall=="Bat"):
        playerOne = int(input("Hit the ball:  "))
        print("")
        playerTwo = choice(runs)

        if(playerOne==playerTwo):
            count=0
            print(f"You are out. Now the opponent will bat.")
            print("")
            print(f"Target for opponent: {playerOneScore}")
            print("")
            batOrBall = swapBatOrBall(batOrBall)
            continue
        else:
            playerOneScore = playerOne+playerOneScore
            print("------------------------")
            print(f"Hit: {playerOne}")
            print(f"Ball: {playerTwo}")
            print(f"Total Score: {playerOneScore}")
            print("------------------------")
            batOrBall = swapBatOrBall(batOrBall)
    elif(batOrBall=="Ball"):
        playerTwo = choice(runs)
        playerOne = int(input("Throw Ball: "))
        print("")

        if(playerOne==playerTwo):
            count=0
            print(f"You are out. Now opponent will ball.")
            continue
        else:
            playerTwoScore = playerTwo+playerTwoScore
            print("------------------------")
            print(f"Hit: {playerTwo}")
            print(f"Ball: {playerOne}")
            print(f"Total Score: {playerTwo}")
            print(f"Target for opponent: {playerOneScore}")
            print("------------------------")
    count+=1

if(playerOneScore<playerTwoScore):
    print("Player 2 is the Winner!")
    print("")
elif(playerOneScore>playerTwoScore):
    print("Player 1 is the Winner!")
    print("")