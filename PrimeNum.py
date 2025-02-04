#Aiden Ramos
#Math 261
#This program will find weather a user's input is true or false



#Default answer if loop does not break is that the answer is prime
ans="\nNumber is prime"

num=int(input("Please enter a number to check if it see if it is prime or composite: "))

for i in range(2,int(num**.5)+1):
    if num%i==0:
        
        #variable reassignment if number is found to be composite and loop breaks
       ans="\nNumber is composite"
       break
    
#displays answer to user
print(ans)