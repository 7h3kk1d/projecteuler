SumOfSquares=0
SquareOfSums=0

for i in range(101):
    SumOfSquares += i**2
    SquareOfSums += i
SquareOfSums**=2
print(SquareOfSums-SumOfSquares)
