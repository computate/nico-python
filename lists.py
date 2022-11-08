'''
Created on May 27, 2021

@author: Nico Tate
'''
import random
if __name__ == '__main__':
    print()
    woman = ["A scientist", "A queen", "A pirate", "A giant rabbit"]
    man = ["A police officer", "An artist", "Your grandfather", "A killer robot"]
    place = ["on Pluto.", "at the supermarket.", "in a spooky, bat-filled cave."]
    sheWore = ["scuba diving gear.", "fairy wings.", "a paper bag."]
    heWore = ["a purple suit.", "a shark costume.", "a beach towel"]
    womenSays = ['"Who are you?"', '"How many beans make five?"', '"Why?"']
    manSays = ['"Beep boop!"', '''Don't eat frogs!"''', '"What time do you call this?"']
    consequence = ["world peace.", "chaos.", "a giant foot squashed them.", "rainbows."]
    worldSaid = ['"Utter nonsense!"', '"Cheese is trending now."', '"BBBRRRRRRRUUUUUUHHHHHHH"', '''"I'm melting!"''']
    while True:
        print(random.choice(woman), "met", random.choice(man), random.choice(place))
        print("She was wearing", random.choice(sheWore))
        print("He was wearing", random.choice(heWore))
        print("She said,", random.choice(womenSays))
        print("He said,", random.choice(manSays))
        print("The consequence was", random.choice(consequence))
        print("The world said,", random.choice(worldSaid))
        print()
        exitChoice = input("Press enter to play again. ")
        if exitChoice.upper() == "EXIT":
            break
        print()
        print("========================================================================================================================================================================")
        print()