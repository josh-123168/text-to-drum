

print("Kick:    '.'\n*\nHi-Hat:  '-'\n*\nSnare:   '_'\n*\nRest:    ' '\n")
beatstring = input("Enter beat loop string (8 characters):")

# def findDash(str):

    
# def findDot(str)
    
# def findUnderscore(str)
    
# def findSpace(str)

def translate(beat):
    beatlist = []
    val = 0
    for symbol in beat:
        if symbol == " ":   # rest
            val = 0
        elif symbol == ".": # kick
            val = 1
        elif symbol == "-": # hat
            val = 2
        elif symbol == "_": # snare
            val = 3
        else:
            return
        beatlist.append(val)
    return beatlist

if (len(beatstring) != 8):
    print("Incorrect string length")
elif translate(beatstring) == None:
    print("Unknown symbols")
else:
    print(translate(beatstring))

# take string at index 1
# search for what symbol
# translate to a value 0-3
# add to a list
# repeat for increasing index


