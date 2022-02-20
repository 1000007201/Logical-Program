import random

stake = int(input("Enter Your Stake:"))
goal = int(input("Enter Your Goal:"))

result = {}
count = 0
wincount = 0
loosecount = 0

while 0 <= stake <= goal:
    option = random.randint(0,1)
    count += 1
    if option == 1:
        wincount += 1
        stake += 1
        result.__setitem__(count,"Win")
    elif option == 0:
        loosecount += 1
        stake -= 1
        result.__setitem__(count,"Loss")
    if stake == 0:
        print("You Losses!!")
        break
    if stake == goal:
        print("You Win!!")
        break

print(f"Win Percentage:{(wincount/count)*100}\nLoss Percentage:{(loosecount/count)*100}")
print(result)