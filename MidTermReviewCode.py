UserInput=int(input("\nPlease enter a whole postive numebr: "))

InputSqr=UserInput**2

def IsPrime(num):
    
    for i in range(2,num):
        if num%i==0:
            return False
        else:
            continue
    return True

primes=[]
for i in range(UserInput,InputSqr+1):
    if IsPrime(i):
        primes.append(i)
    else:
        continue

summ=0
for i in primes:
    summ+=i

def PrintNums(Listt):
    anss=""
    for i in Listt:
        i=str(i)
        anss=anss+" "+i
    return anss
        
        

ans=PrintNums(primes)

print(f"The primes between {UserInput} and {InputSqr} are{ans}.")
print(f"The sum of these primes is {summ}")