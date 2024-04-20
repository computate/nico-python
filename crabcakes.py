def onceCheckForVowels0(onceCheckLetter0):
    if onceCheckLetter0 == "a" or onceCheckLetter0 == "e" or onceCheckLetter0 == "i" or onceCheckLetter0 == "o" or onceCheckLetter0 == "u" or onceCheckLetter0 == "A" or onceCheckLetter0 == "E" or onceCheckLetter0 == "I" or onceCheckLetter0 == "O" or onceCheckLetter0 == "U":
        return "an"
    else:
        return "a"
def onceCheckForVowels1(onceCheckLetter1):
    if onceCheckLetter1 == "a" or onceCheckLetter1 == "e" or onceCheckLetter1 == "i" or onceCheckLetter1 == "o" or onceCheckLetter1 == "u" or onceCheckLetter1 == "A" or onceCheckLetter1 == "E" or onceCheckLetter1 == "I" or onceCheckLetter1 == "O" or onceCheckLetter1 == "U":
        return "an"
    else:
        return "a"
def onceCheckForVowels2(onceCheckLetter2):
    if onceCheckLetter2 == "a" or onceCheckLetter2 == "e" or onceCheckLetter2 == "i" or onceCheckLetter2 == "o" or onceCheckLetter2 == "u" or onceCheckLetter2 == "A" or onceCheckLetter2 == "E" or onceCheckLetter2 == "I" or onceCheckLetter2 == "O" or onceCheckLetter2 == "U":
        return "an"
    else:
        return "a"
def onceCheckForVowels3(onceCheckLetter3):
    if onceCheckLetter3 == "a" or onceCheckLetter3 == "e" or onceCheckLetter3 == "i" or onceCheckLetter3 == "o" or onceCheckLetter3 == "u" or onceCheckLetter3 == "A" or onceCheckLetter3 == "E" or onceCheckLetter3 == "I" or onceCheckLetter3 == "O" or onceCheckLetter3 == "U":
        return "an"
    else:
        return "a"
def onceUponATime(onceParts, story):
    print("\nIf you don't enter anything in one of the inputs, it will end in an error.\n")
    for i in range(len(onceParts)):
        partOfSpeech = onceParts[i]
        onceWords.append(input("%s: " % partOfSpeech))
    onceCheckLetter0 = onceWords[0][0]
    onceCheckLetter1 = onceWords[1][0]
    onceCheckLetter2 = onceWords[8][0]
    onceCheckLetter3 = onceWords[11][0]
    print("\n------\n\nOnce upon %s %s there was %s %s %s that could %s a whole %s with it's %s. This very peculiar %s had a very particular fascination with %s. This became a problem when one day, an explosive %s rolled down a hill, crashed into %s %s, splashed into %s %s pool of %s, and sent the whole town up in %s.\n\nThe End\n"
            % (onceCheckForVowels0(onceCheckLetter0), onceWords[0], onceCheckForVowels1(onceCheckLetter1), onceWords[1], onceWords[2], onceWords[3], onceWords[4], onceWords[5], onceWords[0], onceWords[6], onceWords[7], onceCheckForVowels2(onceCheckLetter2), onceWords[8], onceCheckForVowels3(onceCheckLetter3), onceWords[9], onceWords[10], onceWords[11]))
    story = "Once upon %s %s there was %s %s %s that could %s a whole %s with it's %s. This very peculiar %s had a very particular fascination with %s. This became a problem when one day, an explosive %s rolled down a hill, crashed into %s %s, splashed into %s %s pool of %s, and sent the whole town up in %s.\n\nThe End" % (onceCheckForVowels0(onceCheckLetter0), onceWords[0], onceCheckForVowels1(onceCheckLetter1), onceWords[1], onceWords[2], onceWords[3], onceWords[4], onceWords[5], onceWords[0], onceWords[6], onceWords[7], onceCheckForVowels2(onceCheckLetter2), onceWords[8], onceCheckForVowels3(onceCheckLetter3), onceWords[9], onceWords[10], onceWords[11])
    onceWords.clear()
    print('------\n\nWant to play again? Type in a number that corresponds to a Crab Cake or type in a Crab Cake\'s name.\n\nOr, you can save your Crab Cake for memories by typing "save".\n\nPossible Crab Cakes:\n1. Once Upon a Time\n')
    return story
onceWords = []
comd = 0
onceParts = ["noun", "adjective", "noun", "action verb", "noun", "noun", "action verb ending in -ing", "noun", "noun", "adjective", "liquid", "plural noun"]
story = ""
if __name__ == '__main__':
    print('\nWelcome to the Crab Cakes console (like Mad Libs, but in Python.)\nType "info" for instructions. Type "save" to save "Once Upon A Time" to a file. Please enter the number that corresponds to the Crab Cake or type in the name of the Crab Cake.\n\nHere\'s a list of the possible Crab Cakes you can do:\n\n1. Once Upon a Time\n')
    while True:
        comd = input(']]] ')
        if comd == "info":
            print('\nThe Crab Cakes console (like Mad Libs, but in Python.)\nType "info" for these instructions. Type "save" to save your "Once Upon A Time" to a file. Type in the name of a Crab Cake or it\'s index (number.)\nTo play it, enter an example of the part of speech asked for in the input. (like "noun: pizza")\n\n\nCREDITS:\nGeneral idea, console, and Python features, (like a/an,) by Nico Tate\n\n"Once Upon a Time" by Chris Tate\n\nVersion 1.0')
        elif comd == "1" or comd == "Once Upon a Time":
            story = onceUponATime(onceParts, story)
        elif comd == "save":
            print('\nNotice: You are writing to a file; this means that if you put the path to an existing file, it WILL OVERWRITE IT. Also, unfortunately, you can\'t use ~ to make the path shorter, however, you can use relative paths (if you are in the directory that you want to put the file in.)\n')
            open(input('Please enter a file location (no ~ (see notice)):\n] '), "w").write(story)
        else:
            print('\nUnrecognized command, "%s". Remember, only "info", a number that corresponds to a Crab Cake, or the name of a Crab Cake. Please try again.'%comd)