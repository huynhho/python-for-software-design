# A module is a file that contains a collection of related funcitons grouped together.


##def newLine():
##    print('Most children like sweets')
    
##def threeLine():
##    newLine()
##    newLine()
##    newLine()
##print('First Line.')
##newLine()
##newLine()
##newLine()
##newLine()
##newLine()
##newLine()
##
##print('Second Line.')
##def threeLines():
##    for x in range(3):
##        newLine()

def printTwice(bruce):
    print(bruce, bruce)

def catTwice(part1, part2):
    cat = part1 + part2
    printTwice(cat)
chant1 = "Pie Jesu domine, "
chant2 = "Dona eis requiem."
catTwice(chant1, chant2)
print(cat)
