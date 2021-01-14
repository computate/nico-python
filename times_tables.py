'''
Created on Jan 10, 2021

@author: ctate
'''
if __name__ == '__main__':
    exitChoice = "Nothing"
    while exitChoice.upper() != "EXIT":
        print("Created on January 10, 2021")
        print()
        input("Please enter a times table: ")
        if exitChoice.upper() = "EXIT":
            break
        table = int()
        for x in range(0, 13):
            print(x, "x", table, "=", x*table)
        exitChoice = input("Press return to play again, or type exit to leave.")