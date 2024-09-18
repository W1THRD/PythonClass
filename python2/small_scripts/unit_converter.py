# there are 4 units of currency: iron, gold, emeralds, and diamonds
# lowest unit: iron
# 1 gold = 2 iron
# 1 emerald = 5 gold = 10 iron
# 1 diamond = 8 emeralds = 40 gold = 80 iron

unit_names = ["iron", "gold", "emeralds", "diamonds"]
higher_rates = [0.5, 0.2, 0.125, None] 
lower_rates = [None, 2, 5, 8]

def singleConvert(unit, amount, isHigher):
    if unit < 0 or unit >= len(unit_names):
        print("Error! Not a unit!")
        return(-7439867)
    else:
        if isHigher:
            new_amount = amount * higher_rates[unit]
        else:
            new_amount = amount * lower_rates[unit]
        return(new_amount)

def convert(unitFrom, amountFrom, unitTo):
    if unitFrom < 0 or unitFrom >= len(unit_names):
        print("Error! unitFrom is not a unit!")
    elif unitTo < 0 or unitTo >= len(unit_names):
        print("Error! unitTo is not a unit!")
    else:
        amountTo = amountFrom
        if unitFrom == unitTo:
            print("Already the same unit!")
            return()
        elif unitFrom < unitTo:
            repeats = unitTo - unitFrom
            change = 1
        elif unitFrom > unitTo:
            repeats = unitFrom - unitTo
            change = -1
        else:
            print("This should be impossible!")
        
        current_unit = unitFrom
        for i in range(repeats):
            amountTo = singleConvert(current_unit, amountTo, unitFrom < unitTo)
            current_unit += change
        print(str(amountFrom) + " " + unit_names[unitFrom] + " = " + str(amountTo) + " " + unit_names[unitTo])

def printHelp():
    print("Currencies:")
    print("1 - Iron (lowest unit)")
    print("2 - Gold (1 gold = 2 iron)")
    print("3 - Emeralds (1 emerald = 5 gold = 10 iron)")
    print("4 - Diamonds (1 diamond = 8 emeralds = 40 gold = 80 iron)")
    print()

print("Welcome to currency converter!")
print("This program will convert your currency for you!")
print()

running = True
while running:
    printHelp()
    unitFrom = int(input("Enter unit to convert from: ")) - 1
    amountFrom = int(input("Enter amount of currency to convert from: "))
    unitTo = int(input("Enter unit to convert to: ")) - 1
    convert(unitFrom, amountFrom, unitTo)
    
    again = input("Would you like to convert again? (y/n): ").lower()
    if again == "y":
        print()
    else:
        print("Goodbye!")
        running = False