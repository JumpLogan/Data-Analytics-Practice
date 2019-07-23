import random
r=random.randint(1,3) #For the first random play of the computer.
n=0 #Tracking no of times played
h=0 #Tracking no of times human won
game=['Rock','Paper','Scissors']
human=[0,0,0] #List to capture human's choices
def choice_player ():
    """ Returns the Input of the user (numerical value) after providing few choices."""
    print "Enter your Choice from Below:\n1. Rock\n2. Paper\n3. Scissors\n4. Quit Game\n"
    x=int(raw_input("Choice:"))
    return x
y=choice_player()
while y<=0 or y>4: #To check for any other choices than 1,2,3 and 4
    print "Invalid Response. Enter Again\n"
    y=choice_player()
while y>0 and y<=3:
    n+=1
    human[y-1]+=1 #Storing the input of the human
    if y!=r: #If both choices of computer and human are not equal
        if y-r in (-1,2):
            print "Computer Played--",game[r-1],"--Computer Wins\n"
        else:
            print "Computer Played--",game[r-1],"--You Win\n"
            h+=1
    else:
        print "Computer Played--",game[r-1],"--Game Drawn\n"
    t=[i for i, z in enumerate(human) if z == max(human)] #Storing the indices of a list that is returned by the max function
    r=int(random.choice(t))+1 #To select a random choice by the computer if all 3 have equal chances.
    l=len(t)
    #Below "if" condition is to select computer's next output based on if we have either 1 or 3 maximums from the human list.
    if l in (1,3):
        if r in (1,2):
            r+=1
        else:
            r-=2
    #"Else" condition is to select computer's next output if there are two maximums from the human list.
    else:
        if t==[0,1]:
            r=2
        elif t==[1,2]:
            r=3
        else:
            r=1
    y=choice_player()
    
print "\nQuitting !!!\n\nNo of times played: ",n,"\nNo of times you won: ",h