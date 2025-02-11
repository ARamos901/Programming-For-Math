#Math 261
#Aiden Ramos

import time as T




def gcf(a,b):
    ans=None
    while a!=0:
        r=a%b
        if r==0:
            ans=b
            break
        a=b
        b=r
        
        
    return ans
    








#has the user input their numbers
num1=int(input("Please enter your first number: "))
T.sleep(.5)
num2=int(input("\nPlease enter your second number: "))


#makes sure num1 is the bigger number
if num1<num2:
    temp=num1
    num1=num2
    num2=temp

ans=gcf(num1,num2)
T.sleep(1)

print(f"\nThe greatest common divisor of {num1} and {num2} is {ans}")





    