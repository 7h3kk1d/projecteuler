integers=list(range(2,1000))
last=1000
while True:
    for i in integers:
        for j in integers:
            if j%i==0 and i!=j:
                integers.remove(j)
        if i>integers[-1]**.5:
            break
    if len(integers)>10000:
        break
    else:
        integers=integers+list(range(last,last+1000))
        last += 1000
print(integers[10000])
