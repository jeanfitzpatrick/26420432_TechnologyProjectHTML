print("Your progress in a warfare video game:")
print("You have 10 points to begin with..")
points = 10
count = 0
print("Please enter your stats for the last 5 rounds:")
while count <= 5:
    team = input("Which team won: (O)pponents or (A)llies?")
    team = team.upper()
    if team == "O":
        points -= 1
    elif team == "A":
        points += 1
    else:
        print("Incorrect input")
    OpPlayers = int(input("How many players are left on the opposing team?(0-20)"))
    if OpPlayers >= 15 and OpPlayers < 20:
        points -= 2
    elif OpPlayers >= 10 and OpPlayers < 15:
        points -= 1
    elif OpPlayers >= 5 and OpPlayers < 10:
        points += 1
    elif OpPlayers >= 0 and OpPlayers < 5:
        points += 2
    else:
        print("Incorrect input.")
    APlayers = int(input("How many players are left on the allied team?(0-20)"))
    if APlayers >= 15 and APlayers < 20:
        points += 2
    elif APlayers >= 10 and APlayers < 15:
        points += 1
    elif APlayers >= 5 and APlayers < 10:
        points -= 1
    elif APlayers >= 0 and APlayers < 5:
        points -= 2
    else:
        print("Incorrect input.")
    games = int(input("How many rounds have you previously won?"))
    if games > 20:
        points += 2
    elif games >= 15 and games <20:
        points += 1
    elif games >= 10 and games <15:
        points += 0
    elif games >= 5 and games <10:
        points -= 1
    elif points >= 0 and games <5:
        points -= 1
    else:
        print("Incorrect input.")
    print("Calculating points...")
    print("You have", points ,"points")
    count += 1
newpoints = points - 10
if newpoints >0:
    print("You have improved by", newpoints, "points.")
else:
    print("You have decreased by", newpoints, "points")
print("Based on previous data..")
if newpoints <= 5:
    print("You are 25% more likely to win the next round.")
elif newpoints > 5:
    print("You are 50% more likely to win the next round.")
elif newpoints <+ 0 and newpoints > -5:
    print("You are 25% more likely to lose the next round.")
elif newpoints < -5:
    print("You are 50% more likely to lose the next round.")