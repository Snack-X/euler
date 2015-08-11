MAX = 999

def sumDivisible(n):
  to = MAX / n
  return n * (to * (to + 1)) / 2

print sumDivisible(3) + sumDivisible(5) - sumDivisible(15)
