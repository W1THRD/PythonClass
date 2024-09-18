
consonants = "BCDFGHJKLMNPQRSTVWXYZ"
vowels = "AEIOU"

def reverse(text):
    newtext = ""
    for char in text:
        newtext = char + newtext
    return(newtext)

def getStartEnd(word):
    start = ""
    end = ""
    isStart = True
    for char in word:
        if (char.upper() in consonants) and isStart:
            start += char
        elif not isStart:
            end += char
        else:
            isStart = False 
            end += char
    return((start, end))

def pigLatin(text):
    words = text.split()
    new_words = []
    for word in words:
        start, end = getStartEnd(word)
        new_words.append(end + "-" + start + "ay")
    return(" ".join(new_words))

def ubbiDubbi(text):
    words = text.split()
    new_words = []
    for word in words:
        start, end = getStartEnd(word)
        new_words.append(start + "ubb" + end)
    return(" ".join(new_words))
        
running = True
while running:
    text = input("Enter words or DONE: ")
    if text == "DONE":
        running = False
    else:
        print("Reversed: " + reverse(text))
        print("Pig Latin: " + pigLatin(text))
        print("Ubbi Dubbi: " + ubbiDubbi(text))
    
    print()