##Math 261
#Aiden Ramops
#A function will accept a list as an argument
#And return a new list with the square of the original list
#print the orginal list and the new list in main
#give the user the opportunity to run again


import time as T

def square_fucn(org_list):
    lenn=len(org_list)
    list1=[]
    for j in range(lenn):
        list1.append(org_list[j]**2)
    return list1


N=int(input("\nPlease enter the number of items in your list: "))


while True:
    

    usr_list=[]
    
    for i in range(N):
        num=int(input(f"Please enter number {i+1}: "))
        usr_list.append(num)
    
    new_list=square_fucn(usr_list)
    
    print(usr_list)
    print(new_list)
        
    
    print("\nIf you would like to go again,press enter")
    T.sleep(2)
    #if the user would like to quit, they input Q or q to exit out of the program
    UserStatus=input("\nIf you would like to quit, please enter q: ").lower
    if UserStatus()=="q": 
        break
    
    #this is only used if the user presses enter to contunue
    T.sleep(1.5)