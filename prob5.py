numbers=list(range(2,21))
primes=[2,3,5,7,11,13,17,19]
count=[0]*len(primes)
for i in primes:
    for j in numbers:
        a=0
        while j%i==0:
            j /= i
            a+=1
        if a > count[primes.index(i)]:
            count[primes.index(i)]=a
product=1
for i in range(len(primes)):
    product *= primes[i]**count[i]
print(product)
