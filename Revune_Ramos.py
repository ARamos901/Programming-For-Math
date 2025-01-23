#Aiden Ramos
#Math 261
#Revune
#This program will find the total revune made from notebooks

Rate=3.50


print("This program will tell you the total revune made from notebooks\n")


#Finds how many notebooks were sold in January
JanSales=int(input("Please enter the total number of notebooks sold in January: "))
JanSales=JanSales*Rate
#Finds Revune from January

#Finds how many notebooks were sold in Febuary
FebSales=int(input("Please enter the total number of notebooks sold in Feburay: "))
FebSales=FebSales*Rate
#Finds Revune from Feburay

#displays revune from both months
print(f"The total revune made from notebooks in January were ${JanSales:,.2f}\n")
print(f"The total revune made from notebooks in Febuary were ${FebSales:,.2f}\n")

total=JanSales+FebSales

#adds up the revune from both months and displays to the user
print(f"The total amount of revun3 from the two months are {total:,.2f}")