#Math 261
#Aiden Ramos
#Nnth Prime
#This program will let a user enter a number, and then outputs the Nth prime number

#time so prompts do not show up super fast
import time as T


def IsPrime(Num):
    
    if Num>1:
        #numbers 1 and 0 are not prime
        
    
        #loop to check if the Num is divisible by any number between 2 and half of Num
        for i in range(2,(Num//2)+1):
            if Num%i==0:
                #if any number can be divided into it, it is not prime
                return False
                break
        
        
        else:
            #if it gets out of the loop and here, it is prime
            return True
    else:
        
        return False

#main function
def main():
    #the function will keep going allowing the user to keep inputting numbers
    #unless the user inputs q at the end
    while True:
        UserInput=int(input("\nPlease enter any number between 2 and 100,000: "))
        #keeps track of the prime count
        PrimeCount=0

        for i in range(2,1000000,1):
            #calls the IsPrime function
            if IsPrime(i):
                #if the function returns True, the count is incremnted by 1
                PrimeCount+=1
                if PrimeCount==UserInput:
                    #once the prime count matches the User inputted number, it outputs
                    #the information, and breaks the loop
                    print(f"\nThe number {UserInput} prime number is {i}.")
                    T.sleep(3)
                    break
        
        #Prompts the user if they would like to continue
        print("\nIf you would like to check another number,press enter")
        T.sleep(2)
        #if the user would like to quit, they input Q or q to exit out of the program
        UserStatus=input("If you would like to quit, please enter q: ").lower
        if UserStatus()=="q": 
            break
        
        #this is only used if the user presses enter to contunue
        T.sleep(1.5)

#calls main function
main()

        
                
    
