import random
# for some reason python's normal division gives some strange results
from decimal import Decimal
release_chance=0
# Number of times you want to experiment higher the better accuracy
iterations=int(input("Number of Iterations(Anything above 100000 takes a long time):"))
for x in range(iterations):
    # fill boxes with number 1 to 100 no repeating
    boxes = random.sample(range(1, 101), 100)
    #initialise release as True
    release = True
    #for each prisoner with number 1 to 100
    for prisoner in range(1,101):
        #initial box to be opened is of number of prisoner
        box = prisoner
        #initialize found as False
        found = False
        #iterate 50 times as each prisoner got 50 chances
        for chance in range(50):
            #if the box contain same number as that of prisoner
            if(boxes[box-1]==prisoner):
                found = True
                #his work is done so game awaits next prisoner
                break
            else:
                #otherwise he goes to next box with number that he/she saw in previous box
                box = boxes[box-1]
        #if any prisoner failed to find his/her number
        if(found == False):
            #then game is over
            release = False
            break
    # if release is true increment release chance
    if(release==True):
        release_chance = release_chance+1
#calculate percentage and print
per = (Decimal(release_chance)/Decimal(iterations))*100
print(per," cases they were realsed")