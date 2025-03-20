#Roll Die Simulation
#Aiden Ramos
#Math 261

import random as R
import time as T


def roll(numm):
    num=R.randint(1, 6)
    
    if num==numm:
        return True
    else:
        return False

rolls=int(input("Please enter how many times you would like to roll the die: "))
T.sleep(1)
UserNum=int(input("Please enter what number you would like to test the probability for: "))

count=0
    
    
print("\nThis program will run a simulation of rolling one die.")
T.sleep(1)
print(f"\nThe simulation will run {rolls} times.")
T.sleep(1)

for i in range(rolls+1):
    if roll(UserNum):
        count+=1

T.sleep(1)

print(f"\nA {UserNum} was rolled {count} times out of the {rolls} rolls.")
T.sleep(1)
print(f"\nThe probability of rolling a {UserNum} in this instance of the simulation is:")
print(f"{count/rolls:.2f}")
