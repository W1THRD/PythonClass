
names = []
scores = []

def printScore(index):
    print(names[index] + ": " + str(scores[index]))

def printScores(full):
    print()
    length = len(scores)
    if full:
        print("SCORE SUMMARY")
        print("--------------------------")
        print("TOTAL NUMBER OF SCORES: " + str(length))
        searchScores(False)
        searchScores(True)
        
    print()
    print("ALL SCORES")
    print("--------------------------")
    for i in range(length):
        printScore(i)

def addPlayer():
    name = input("Enter name: ")
    valid = False
    score = 0
    while not valid:
        try:
            score = int(input("Enter score: "))
            valid = True
        except:
            print("Error: not an integer. Try again.")
            valid = False
    names.append(name)
    scores.append(score)
    
def searchScores(lowest):
    search = scores[0]
    foundNames = []
    for i in range(len(names)):
        if lowest and scores[i] < search:
            search = scores[i]
            occurences = 1
            foundNames = []
            foundNames.append(names[i])
        elif (not lowest) and scores[i] > search:
            search = scores[i]
            foundNames = []
            foundNames.append(names[i])
        elif scores[i] == search:
            foundNames.append(names[i])
    
    message = ""
    if lowest:
        message += "LOWEST SCORE: "
    else:
        message += "HIGHEST SCORE: "
    for i in range(len(foundNames)):
        name = foundNames[i]
        message += name
        if i == len(foundNames) - 1:
            message += ": "
        elif i == len(foundNames) - 2:
            if len(foundNames) > 2:
                message += ", and "
            else:
                message += " and "
        else:
            message += ", "
    
    message += str(search) + " points."
    print(message)

def printCommands():
    print("---- MENU ----")
    print(" 1: Enter a new player & score")
    print(" 2: Get the current highest score")
    print(" 3: Get the current lowest score")
    print(" 4: Print all scores")
    print(" 5: Print a full summary")
    print(" 0: Quit")

def handleCommand(cmd):
    if cmd == 1:
        addPlayer()
    elif cmd == 2:
        searchScores(False)
    elif cmd == 3:
        searchScores(True)
    elif cmd == 4:
        printScores(False)
    elif cmd == 5:
        printScores(True)
    else:
        print("Error: command does not exist.")

running = True
while running:
    printCommands()
    
    try:
        cmd = int(input("Enter your command number: "))
    except:
        cmd = 666
        print("Error: not a number. Try again.")
    
    if not cmd == 666:
        if cmd == 0:
            running = False
        else:
            handleCommand(cmd)
    
    print("")
    