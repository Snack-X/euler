to = 100

sumOfSquare = sum(map(lambda a: a * a, range(to + 1)))
squareOfSum = sum(range(to + 1)) ** 2

print squareOfSum - sumOfSquare