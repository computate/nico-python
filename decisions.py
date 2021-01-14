import random
if __name__ == '__main__':
    exitChoice = "nothing"
    while exitChoice != "EXIT":
        print("")
        print("--------------------------------------------------------------------------------------------")
        print("")
        print("You are in a mysterious castle.")
        print("In front of you are four doors You must choose one")
        playerChoice = input("1, 2, 3 or 4...")
        if playerChoice == "1":
            print("You find a room full of treasure. You're rich!")
            print("GAME OVER, YOU WIN!")
        elif playerChoice == "2":
            print("The door opens and an angry ogre hits you with his club.")
            print("GAME OVER. YOU LOSE!")
        elif playerChoice == "3":
            print("You go into the room and find a sleeping dragon.")
            print("You can either:")
            print("1) Try to steal some of the dragons gold.")
            print("2) try to sneak around the dragon to the exit.")
            dragonchoice = input("Type 1 or 2...")
            if dragonchoice == "1":
                print("The dragon wakes up and eats you. You are delicious.")
                print("GAME OVER. YOU LOSE!")
            elif dragonchoice == "2":
                print("You sneak around the dragon and escape the castle, blinking in the sunshine.")
                print("GAME OVER! YOU WIN!")
            else:
                print("There has been an error with your request. Please try again.")
        elif playerChoice == "4":
            print("You enter a room with a sphinx.")
            print("It asks you to guess what number it is thinking of, between 1 and 10.")
            number = int(input("what number do you choose?"))
            if number == random.randint(1,10):
                print("The sphinx hisses in disappointment. You guessed correctly.")
                print("She must let you go free.")
                print("GAME OVER. YOU WIN!")
            else:
                print("The sphinx tells you that you are incorrect.")
                print("YOu are now her prisoner forever.")
                print("GAME OVER. YOU LOSE!")
        else:
            print("There has been an error with your request. Please try again.")
        exitChoice = input("Press return to play again, or type EXIT to leave.")