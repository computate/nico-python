'''
Created on Feb 15, 2022

@author: ctate
'''

if __name__ == '__main__':
    print("Created on Feb 15, 2022")
    print()
    powers = {"The Pigeon": "flight", "Brainzar": "mind reader", "Cyborg": "controls machines"}
    print (powers["The Pigeon"])
    powers["Laser Girl"] = "shoots lasers"
    print(powers)
    del powers["The Pigeon"]
    powers["Brainzar"] = "seeing the future"
    print(powers)
    