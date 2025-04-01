#Aiden Ramos
#Factor Sum
#Math 261
import time as T
#function to get factors and get the sum of them
def Get_Factors(num):
    #list to hold factors
    facts=[]
    #loops through the numbers up to the number but excluding the actual num
    for i in range(1,num):
        #if the current number in the range is a factor
        #it is appended to the factor list
        if num%i==0:
            facts.append(i)
    #gets the sum of the factors
    summ=sum(facts)
    #returns the sum of the factors
    return summ



while True:
    #sets all counts to zero
    deff=0
    perfect=0
    abun=0
    #gets user num to loop through
    UserNum=int(input("Please enter a number between 2 and 100: "))
    #loop to look for differant numbers
    for i in range(2,UserNum+1):
        #calls function holds the sum in a variable
        CurSum=Get_Factors(i)
        #finds where the sum falls
        if CurSum>i:
            abun+=1
        elif CurSum==i:
            perfect+=1
        else:
            deff+=1
    
    T.sleep(1)
    #rounds and moves the decimal place over for each result
    deff=round((deff/UserNum)*100,2)
    perfect=round((perfect/UserNum)*100,2)
    abun=round((abun/UserNum)*100,2)
    
    #prints the results to the user
    print(f"\nThe % of numbers between 2 and {UserNum} that are abundant sum factors is {abun}%.")
    T.sleep(1.5)
    print(f"\nThe % of numbers between 2 and {UserNum} that are deficient sum factors is {deff}%.")
    T.sleep(1.5)
    print(f"\nThe % of numbers with between 2 and {UserNum} that are perfect sum factors is {perfect}%.")
    T.sleep(2)
    #asks the user if they would like to try again
    print("\nIf you would like to enter another number, please hit enter.")
    T.sleep(1)
    #makes the user input lower
    UserStatus=input("If you would like to quit, please enter Q: ").lower()
    if UserStatus=="q":
        break
    
    

