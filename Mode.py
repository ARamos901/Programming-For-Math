#Math 261
#Aiden Ramos
#This program will find the mode of a list

#Gets the amount of items the user wants in the list from the user
ListLen=int(input("Please enter the amount of items you would like in your list: "))
#user list
UserList=[]
#loop to put the items in the list
for i in range(ListLen):
    num=int(input(f"Please enter number {i+1} in the list: "))
    UserList.append(num)

#sorts the list for the logic to work properly
UserList.sort()

#Starts the longest mode variables as zero and none 
Long_Mode=None
LongMode_Count=0

#makes the first item in the list the mode for now 
Cur_Mode=UserList[0]
Cur_ModeCount=1

#starts the loop at the second element since the first element is the current mode
for i in UserList[1:]:
#if i is the current mode it increments the count by 1
    if i==Cur_Mode:
        Cur_ModeCount+=1
    else:
        #if i does not equal to the current mode it checks to see
        #if the last modes counts were larger than the largest modes
        if Cur_ModeCount>LongMode_Count:
            Long_Mode=Cur_Mode
            LongMode_Count=Cur_ModeCount
    
    #    Resets the current mode variables to start again
        Cur_ModeCount=1
        Cur_Mode=i

#checks the values again after the loop
if Cur_ModeCount>LongMode_Count:
    Long_Mode=Cur_Mode
    LongMode_Count=Cur_ModeCount

        
print(f"\nThe mode in your list is {Long_Mode} with it appearing in the list {LongMode_Count} times.")
    
    