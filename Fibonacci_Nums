from functools import cache

#use cache to increase efficiency 
@cache
def fibonacci(n):
    #if the user's num is 0, the Fib numn is 1
    if n == 0:
        return 1 
    #if the user inputs 1, the Fib number is 2 
    elif n == 1:
        return 2  
    else:
      #this is the logic of Fibonacci nums
        return fibonacci(n - 1) + fibonacci(n - 2)

# Ask user for input
try:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Please enter a non-negative integer.")
    else:
        print(f"The Fibonacci number for {num} is {fibonacci(num)}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
