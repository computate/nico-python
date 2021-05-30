'''
Created on Jan 10, 2021

@author: Nico Tate
'''
if __name__ == '__main__':
    exitChoice = "Nothing"
    while exitChoice.upper() != "EXIT":
        exitChoice = input("Please enter a times table: ")
        if exitChoice.upper() == "EXIT":
            break
        if not exitChoice.isnumeric():
            print()
            print("That is not a times table. Please try again.")
            print("==============================================================================================================================================================================================")
        if exitChoice.isnumeric():
            table = int(exitChoice)
            for x in range(0, 13):
                print(x, "x", table, "=", x*table)
                print("==============================================================================================================================================================================================")