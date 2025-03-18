#random number
#Aiden Ramos
#Math 261

import random as R
import time as T

RandNum=R.randint(1, 100)

UserNum=None

while RandNum!=UserNum:
    T.sleep(1)
    UserNum=int(input("\nPlease guess the random number in the range of 1-100: "))
    T.sleep(1)
    
    if UserNum<101 and UserNum>0:
        
        if UserNum==RandNum:
            print(f"\nCorrect! The random number was {RandNum}.")
            break
        
        if UserNum>RandNum:
            print("\nThe random number is lower than the number you guessed.")
            T.sleep(1)
            print("\nPlease try again.")
            continue
        
        if UserNum<RandNum:
            print("\nThe random number is higher than the number you guessed.")
            T.sleep(1)
            print("\nPlease try again.")
            continue
    
    else:
        print("Please enter a valid number to guess.")
        T.sleep(1)
        continue
            
                