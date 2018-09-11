import sys

# Iterating through all the keyword arguments
for arg in sys.argv[1:]:

    # Opens file and reads to varibable
    file = open(arg, "r+")
    text = file.read()
    file.close()
    # Splits text into a list with all the lines
    lines = text.split("\n")
    # Checks for empty last line because of a UNIX standard to add an empty
    # line
    if (lines[-1] == ""):
        lines = lines[:-1]
    # Initiates counters
    linecount = len(lines)
    wordcount = 0
    charcount = 0
    # Nested forloop for looping through each word
    for line in lines:
        for word in line.split(" "):
            # It was counting empty strings as words. Not anymore!
            if word != "":
                wordcount += 1
                charcount += len(word)

    print(linecount, wordcount, charcount, arg)
