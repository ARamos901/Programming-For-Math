#Math 261
#Aiden Ramos

# school hallway has 100 lockers along the wall, initially all closed. One person walks down the hall and
#opens every locker.A second person walks down and closes every second locker. A third person changes
#the state of every third locker (opens it if it’s closed, and closes it if its’s open).
#A fourth person changes the state of every fourth locker. And so on.

#This program will print out what lockers will be open after the 100th person passes through.





#creates a list of 100 closed lockers
closed=[False]*101

#create a list for open lockers
openn=[]

#loop for each person walking through the hallway
for p in range(1, 101):
    #loop to know what locker each person will open or close in the hallway
    for v in range(p, 101, p):
        #changes value of locker 
        closed[v] = not closed[v]  

#loops through the range of the lockers to get each individual locker numver
for i in range(1,101):
    #if the locker is found True(open) it appends it to the openn list
    if closed[i]:
        openn.append(i)
      
#prints output to user
print(f"The open lockers are lockers {','.join(map(str, openn))}")