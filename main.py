#Hand Cricket Game
from random import choice

print("---------------------------------")
print("")
print("Welcome to the hand cricket game.")
print("")
print("---------------------------------")

coin = ["Heads","Tails"]
runs = [1,2,3,4,6]
playerOneScore = 0
playerTwoScore = 0 
count = 1

#-------------------------------------------------------------

def coinToss(headsOrTails):
    flip = choice(coin)
    if(flip==headsOrTails):
        print("Player 1 won the toss!")
        print("")
        print("-----------------------------------")
        return True
    else:
        print("Player 2 won the toss!")
        print("")
        print("-----------------------------------")
        return False


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

print("")
if(coinToss(headsOrTails)):
    batOrBall = input("Would you like to Bat or Ball?: ")
else:
    batOrBall = "Bat"
    print("Player 2 has decided to Ball.")
print("")

if(batOrBall=="Bat"):
    print("You are batting first.")
    print("")
    print("-----------------------------------")
elif(batOrBall=="Ball"):
    print("You are bowling first.")
    print("")
    print("-----------------------------------")



while(count<=overs*6):
    if(batOrBall=="Bat"):
        playerOne = int(input("Hit the ball:  "))
        print("")
        playerTwo = choice(runs)

        if(playerOne==playerTwo):
            count = 1
            print(f"You are out. Now the opponent will bat.")
            print("")
            print("------------------------")
            print(f"Hit: {playerOne}")
            print(f"Ball: {playerTwo}")
            print(f"Balls Remining: 0")
            print(f"Total Score: {playerOneScore}")
            print("------------------------")
            print(f"Target for opponent: {playerOneScore}")
            print("")
            batOrBall = swapBatOrBall(batOrBall)
            continue
        else:
            playerOneScore = playerOne+playerOneScore
            print("------------------------")
            print(f"Hit: {playerOne}")
            print(f"Ball: {playerTwo}")
            print(f"Balls Remining: {overs*6-count}")
            print(f"Total Score: {playerOneScore}")
            print("------------------------")
            if(count==overs*6):
                count = 1
                batOrBall = swapBatOrBall(batOrBall)
                print("Now player 2 is batting.")
                continue

    elif(batOrBall=="Ball"):
        playerTwo = choice(runs)
        playerOne = int(input("Throw Ball: "))
        print("")

        if(playerOne==playerTwo):
            count=0
            print(f"Player 2 is out.")
            print("")
            print("------------------------")
            print(f"Hit: {playerOne}")
            print(f"Ball: {playerTwo}")
            print(f"Balls Remining: {overs*6-count}")
            print(f"Total Score: {playerOneScore}")
            print("------------------------")
            continue
        else:
            playerTwoScore = playerTwo+playerTwoScore
            print("------------------------")
            print(f"Hit: {playerTwo}")
            print(f"Ball: {playerOne}")
            print(f"Balls Remining: {overs*6-count}")
            print(f"Total Score: {playerTwoScore}")
            print("------------------------")
            if(playerTwoScore>playerOneScore):
                print("Player 2 won this game!")
                quit()
    count+=1

if(playerOneScore<playerTwoScore):
    print("Player 2 is the Winner!")
    print("")
elif(playerOneScore>playerTwoScore):
    print("Player 1 is the Winner!")
    print("")