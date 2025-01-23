#Aiden Ramos
#Math 261
#Wages
#User will input their name, how many hours they worked, and their hourly rate and the program 
#will output their weekly wage

name=str(input("Please enter your name: "))

HrsWrked=float(input("Please enter how many hours you worked: "))

HrRate=float(input("Please enter what your hourly rate is: "))

result=HrRate*HrsWrked

print(f"{name}, you worked {HrsWrked} hours this week and earned ${result:.2f}.")
