from math import ceil, floor
def palindrome(n):
    string=str(n)
    if string[:floor(len(string)/2)]==string[ceil(len(string)/2):][::-1]:
        return True
    else:
        return False

largest=0
for i in range(1000):
    for j in range(1000):
        if i*j>largest and palindrome(i*j):
            largest=i*j


print(largest)
