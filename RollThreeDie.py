#Aiden Ramos
#Math 261
#Rolling Three Die
import time as T

import random as R


def roll():
    ans=[]
    
    #Roll Two variable
    RollTwo=False
    
    #makes list for die
    Die=[]
    #rolls first die and appends it to list
    Die1=R.randint(1, 6)
    Die.append(Die1)
    
    #rolls second die and append to list
    Die2=R.randint(1, 6)
    Die.append(Die2)
    
    #rolls second die and appends to list
    Die3=R.randint(1, 6)
    Die.append(Die3)
    
    #sorts the list
    Die.sort()
    #if there is a two in the die, it changes to true
    if 2 in Die:
        RollTwo=True
    
    #takes the smallest value out of the list
    smallest=Die[0]
    #appends both answers to the ans list
    ans.append(smallest)
    ans.append(RollTwo)
    #returns the list
    return ans
    

#count for the number of times two is rolled
TwoCount=0
#Avgerage variable
LowestAvg=0
#rolls die 500 times
for i in range(501):
    ans=roll()
    #puts both of the answers in two differant variables
    ans1=ans[0]
    ans2=ans[1]
    #adds the lowest from the current roll to the average variable
    LowestAvg+=ans1
    #if there was a two, it increments the count by 1
    if ans2:
        TwoCount+=1

#gets the average
LowestAvg=LowestAvg/500
#prints out two count
T.sleep(2)
print(f"\nAt least one 2 is rolled {TwoCount} times out of 500 trials")
T.sleep(3)
#finds the probablity
TwoCount=TwoCount/500
TwoCount=TwoCount*100
#prints the probability
print(f"\nThe probability of rolling at least one 2 is {TwoCount}%")
T.sleep(1.5)
#prints the average
print(f"and the average value of the smallest die is {LowestAvg:.2f}")



   




    



    
    
