#Game List Set Up

#Character Creation : Start of Game

fnames = []
lnames = []
ages = []
sexs = []
assigns = []
hunger = []
life = []
alive = "alive"
dead = "dead"
work = "null"
hungry = True
turn  = 0

village = raw_input("Please name your village: ")
pop = input("How many people are there in the village? ")

for i in range(pop):
    print ("Person ", i)
    fname = raw_input("Enter first name: ")
    fnames.append(fname)
    lname = raw_input("Enter last name: ")
    lnames.append(lname)
    age = input("Enter age (between 11 and 15): ")  #Come back to enforce age range
    ages.append(age)
    sex = raw_input("Enter sex: ")
    sexs.append(sex)
    assigns.append(work)
    hunger.append(hungry)
    life.append(alive)

i = input ("Enter a person's number to print out their info ")
print fnames[i], lnames[i], ages[i], sexs[i], assigns[i], hunger[i]



#Resouces

foodsupplies = 2
oresupplies = 0
woodsupplies = 0
babiesbirthed = 0
metalsupplies =0

print "This is the first turn."

def starve(foodsupplies, pop):
    print "The youngest die first. Until I figure out a way to let you choose"
    for i in range(foodsupplies):
        hunger[i] = False
        foodsupplies -= 1
        print fnames[i], lnames[i], "has been fed."
    for i in range(pop):
        if hunger[i] == True:
            print fnames[i], lnames[i], "has starved to death."
            life[i] = dead

def feed(foodsupplies, pop):
    if pop > foodsupplies:
        print ("Your people are starving my lord.")
        starve(foodsupplies, pop)
    else:
        for i in range(pop):
            hunger[i] = False
            foodsupplies -= 1
            print fnames[i], lnames[i], " has been fed."
    print "You have", foodsupplies, "food left."
    

feed(foodsupplies, pop)

#The above works!
        
def assignments(pop, assigns):
    print ("Choosing an assignment")
    print """
      "Log"   Logging         +1 Wood
      "Baby"  Midwifery       +1 Person
      "Food"  Farming         +3 Food
      "Ore"   Mining           +1 Ore
      DON'T PICK BABY,  I HAVEN'T MADE IT YET
     """
    # "Metal" Blacksmithing   Turn 1 ore to 1 metal
    for i in range(pop):
        print fnames[i], lnames[i], "needs a job."
        work = raw_input("Enter a job: ")
        working(work, fname)

def working(work, fname):
    if work == "Log":
        woodsupplies += 1
    if work == "Food":
        foodsupplies += 3
    if work == "Ore":
        oresupplies += 1

def turnEnd():
    print "It is the", turn, "year of", village
    print "There are", pop, "people in the village right now."
    print "Everyone has been fed and you have", foodsupplies, "remaining."
    print "Resource Update:"
    print "Wood:", woodsupplies
    print "Ore:", oresupplies
    #newturn(turn)

#Baby Stuff

#Function: viableOffspring
#def viableOffspring(person1, person2):
#    if people[person1][2] != people[person2][2] and population < 50:
#        return True #having a child is possible
#    elif people[person1][2] == people[person2][2] and population < 50:
#        print ("Only a man and woman produce viable offspring. Try again.")
#        return False
#    else:
#        return False #having a baby is not possible


#Function: createChild, might make another funciton midwife that calls createChild,
#so that the nested if statement doesn't drive me crazy!!!
#def createChild(person1, person2):
#   if viableOffspring(person1, person2) == True:
#        fname = input("What is this child's first name: ")
#        FirstNames.append(fname)
#        lname = people[person1][1] "-" people[person2][1]
#        LastNames.append(lname)
#        sex.append(rand)

#Make a random number
def rand():
    x = random.randint(1,2)
    if x / 2 == 1:
        print ("Girl")
    else:
        print ("Boy")
    print (x)
