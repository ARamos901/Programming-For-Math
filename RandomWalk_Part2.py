#Random Walk
#Math 261
#Aiden Ramos

import random as R
#number of steps and walks
steps=1
walks=5000
#function that is called for each
def Step():
    #gets the random step
    RandomStep=R.randint(0, 100)
    #if the random step is 51 or greater, it is true
    if RandomStep>=51:
        return True
    #if not, it returns false
    else:
        return False
        
#steps have to incremnt up to take
StepsToTake=25

for i in range(1,StepsToTake+1):
    #Counters to hold the distance 
    EndPointCounter=0
    StartingPointCounter=0
    for i in range(0,walks):
        #holds the distance for each walk, in addition to resets the distance for each walk
        dist=0
        #loop to simulate steps
        for i in range(steps):
            #if the Step function returns true it adds 1 to the distance
            if Step():
                dist+=1
                #checks to see if the distance is zero to for the starting point counter
                if dist==0:
                    StartingPointCounter+=1
            else:
                #if the function does not return true it subtracts from the distance
                dist-=1
                #checks to see if the distance is zero to for the starting point counter
                if dist==0:
                    StartingPointCounter+=1
        #gets the absoulte value from the distance to add to the EndPoint counter variable
        dist_startingPoint=abs(dist)
        EndPointCounter+=dist_startingPoint
        
        #outputs the answers to the user
    print(f"\nFor the simulation for the amount of steps {steps}:")
    print(f"The average distance from the starting point is {EndPointCounter/walks:.2f} steps")
    print(f"During the random walk, the average number of times the walker returned to the starting point is {StartingPointCounter/walks:.2f} times.")
    #to go up in the amount of steps taken per walk
    steps+=1
        
        
    

        