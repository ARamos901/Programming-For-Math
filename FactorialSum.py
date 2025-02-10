#Aiden Ramos
#Math 261
#Factorial Sum
#This program has the user enter a number between 3 and 20 and then outputs the sum of each numbers
#factorial from 1 to the users number

import time as T

def Factorial(Fact_Num):
    #this function will get the factorial of the current number
    
    #base case for recursive function
    if Fact_Num==0 or Fact_Num==1:
        return 1
    else:
        #recursive part of function to multiply the current argument by the current number
        return Fact_Num*Factorial(Fact_Num-1)
        


#prompts user to input a number to get the factorial sum
num=int(input("\nPlease enter a number between 3 and 20: "))
    
#sum of the Factorials
Fact_sum=0
    
for i in range(1,num+1):
#Call to the Factorial function with the current number in the range as the argument
    Fact_sum+=Factorial(i)
    
#sleep for function so the output does not just come out immediately
T.sleep(1.5)

#outputs result to user    
print(f"\nThe sum of the factorials 1 to {num} is {Fact_sum:,}")