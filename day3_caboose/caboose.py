import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if(n%i==0):
            return False
    return True

def isCaboose(n):
    prime = 0
    for i in range(1, n+1):
        x = i**2 - i + 41
        if not (isPrime(x)):
            return False
        prime += 1
    return True

def caboosePrimeRatio(n):
    prime_count = 0
    for i in range(1, n + 1):
        x = i**2 - i + 41
        if isPrime(x):
            prime_count += 1
    return prime_count / n

n = 100
for i in range(1,n):
    if(isCaboose(i)):
        print(f"{i} is Caboose")
    else:
        print(f"{i} is not Caboose")
    print(f"Caboose ratio for {i} is {caboosePrimeRatio(i)}")