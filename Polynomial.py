#Aiden Ramos
#Math 261
#Polynomial

#time module
import time as T

#function to calucate values
def calcuc(val1,val2,val3,val4,x):
    #rounds to two decimal places and returns to main
    return round(val1*x**3+val2*x**2+val3*x+val4,2)



#list to hold coefficents
nums=[]
#gets all of the coefficentss and 
#puts them in the list as long as they are not zero
print("\nPlease enter the coefficients for the polynomial.")
T.sleep(2)
a=float(input("Please enter a coefficient for x^3 : "))
if a!=0:
    nums.append(f"{a}x^3+")
T.sleep(1)
b=float(input("Please enter a coefficient for x^2 : "))
if b!=0:
    nums.append(f"{b}x^2+")
T.sleep(1)
c=float(input("Please enter a coefficient for x : "))
if c!=0:
    nums.append(f"{c}x+")
T.sleep(1)
d=float(input("Please enter a constant term : "))
lenn=len(nums)
#if the list does not have any current values in it, it will
#at least put a zero in it so it has a ceoefficent
if d!=0 or lenn==0:
    nums.append(f"{d}")
T.sleep(1)
    
#joins the values from the list together into one variable to get the polynomial
#the replace is so the numbers look right together when they are joined together
poly=" ".join(nums).replace("+ -","-").replace("+ ","+")
print("\nThe polynomial is:")
#prints the polynomial
print(f"f(x)={poly}")
T.sleep(1.5)

while True:
    #asks user for value of x
    x=int(input("\nPlease enter a value for x: "))
    T.sleep(1)
    #prints the result from the function
    print(f"tThe results from plugging in the value {x} is:")
    print(f"f({x})=",calcuc(a,b,c,d,x))
    
    
    #asks the user if they would like to try again
    print("\nIf you would like try another value for x, press enter")
    T.sleep(2)
    Status=input("If you would like to quit, enter q: ").lower()
    if Status=="q":
        break
    
    