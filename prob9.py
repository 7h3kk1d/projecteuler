for c in range(500):
    for a in range(500):
        b=1000-a-c
        if a*a+b*b==c*c:
            print(a*b*c)
            break
