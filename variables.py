'''
Created on Sep 17, 2019

@author: ctate
'''

if __name__ == '__main__':
    print("create your character ")
    name = input("what is your character called? ")
    age = input("how old is your character? ")
    strengths = input("what are your character's strengths? ")
    weaknesses = input("what are your character's weaknesses? ")
    print("\n\nyour character's name is %s" % name)
    print("your character is %s years old" % age)
    print("strengths: %s" % strengths)
    print("weaknesses: %s" % weaknesses)
    print('%s says, "thanks for creating me!"' % name)