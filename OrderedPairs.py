#Aiden Ramos
#Math261
#This program will have the user inputa whole number and the program will output
# all possible ordered pairs between (a,b)

num=int(input("Please enter a whole number to find all possible ordered pairs: "))

for cols in range(1,num+1):
    print("\n")
    for rows in range(1,num+1):
        print(f"({cols},{rows})",end=" ")
        
        