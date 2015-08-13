import euler

amicable = []

def d(n):
  return sum(euler.divisors(n))

for i in range(2, 10000):
  if d(i) not in amicable and i == d(d(i)) and d(i) != d(d(i)):
    amicable.append(i)
    amicable.append(d(i))

print sum(amicable)
