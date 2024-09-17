
import sys

print("COOLNESS TEST")
coolness = 0

a = input("Do you like cats (y/n)?").lower()

if a == "y":
    coolness += 1
elif a== "n":
    coolness -= 1
else:
    print("Error: invalid answer")
    sys.exit()
    
a = input("Do you like dogs (y/n)?").lower()

if a == "y":
    coolness -= 1
elif a== "n":
    coolness += 1
else:
    print("Error: invalid answer")
    sys.exit()

a = input("Do you like Minecraft (y/n)?").lower()

if a == "y":
    coolness += 1
elif a== "n":
    coolness -= 1
else:
    print("Error: invalid answer")
    sys.exit()
    
if(coolness > 0):
    print("You are cool.")
    cool = True
else:
    print("You are not cool.")
    cool = False
    
print("Wait... your evil twin from an alternate universe arrived")
if(not cool):
    print("Your evil twin is cooler than you, I\'ll go hang out with him.")
else:
    print("You are cooler than the evil twin, I\'ll tell him to get lost.")
    