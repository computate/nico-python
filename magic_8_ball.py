'''
Created on May 29, 2021

@author: ctate
'''

if __name__ == '__main__':
    playChoice = "nothing"
    exitchoice = "nothing"
    eightBall = ["It is certain."
                , "It is decidedly so."
                 , "Without a doubt."
                 , "Yes definitely."
                 , "You may rely on it."
                 , "As I see it, yes."
                 , "Most likely."
                 , "Outlook good."
                 , "Yes."
                 , "Signs point to yes."
                 , "Reply hazy, try again."
                 , "Ask again later."
                 , "Better not tell you now."
                 , "Cannot predict now."
                 , "Concentrate and ask again."
                 , "Don't count on it."
                 , "My reply is no."
                 , "My sources say no."
                 , "Outlook not so good."
                 , "Very doubtful."
                ]
    exitChoice = input()
    if exitChoice.upper() == "EXIT":
        break
    elif exitChoice.upper() == "HELP":
        print("HELP MENU:")
        print()
        print("I only answer yes or no questions.")
        print("Please do not use me for actual questions that you need to know the answer to.")
        print('To play after opening help menu, run the program again or enter "play".')
        if playChoice.upper() == "PLAY":
            input(random.choice(eightBall))
    else:
        print(random.choice(eightBall))