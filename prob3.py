from math import sqrt, ceil

num=600851475143
max_prime=1
for i in range(2,ceil(sqrt(num))):
    if num % i == 0:
        max_prime=i
    while num % i == 0:
        num /= i
print(max_prime)
