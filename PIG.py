#Aiden Ramos
#Math 261

import random as R
import time as T


print("\nThis program plays the game of PIG.")
T.sleep(1.5)
print("One die is rolled.You decide when to stop rolling.")
T.sleep(1.5)
print("You find the sum of the rolls,however...")
T.sleep(1.5)
print("If you roll a 1, the turn is over and you have no points.")
SumPts=0
GamesPlayed=500

UserNum=int(input("\nPlease enter the number thesehold for the points: "))


for i in range(1,GamesPlayed+1): 
    total=0
    #total to count pts for eacg game
    while (total<UserNum):
        
        
        #gets random roll
        die=R.randint(1, 6)
        
        
        #if the user rolls a one, the turn is over and they get no points
        if die==1:
            total=0
            break
        else:
            #adds current roll to total
            total+=die
        
        
        
        
        
        
    #adds total to sum of points
    SumPts+=total

AvgPts=SumPts/GamesPlayed
print(f"\nThe average amount of points rolled by the games is {AvgPts:.2}")