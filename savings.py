#Math 261
#Aiden Ramos
#This program will have the user input three numbers to find how long it would take to gain their
#desired amount of money

import time as T


#user inputing values for savings account
StrtMoney=float(input("Please enter the amount of money you start with in your savings account:$"))

T.sleep(1)

APR=float(input("\nPlease enter your savings annual APR: "))

T.sleep(1)

GoalMoney=float(input("\nPlease enter the goal savings account value you would like to achieve:$"))

T.sleep(1)

Yr=0


while StrtMoney<GoalMoney:
    MnyEarnedYrly=StrtMoney*APR
    StrtMoney+=MnyEarnedYrly
    Yr+=1
    print(f"\nAfter year {Yr} the balance in your bank account is {StrtMoney:,.2f}")
    T.sleep(.5)

T.sleep(1)
print(f"\nIt took {Yr} year's to reach the desired balance")