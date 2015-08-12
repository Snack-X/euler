amicable = []

def d(n):
  divisors = []
  for i in range(1, n):
    if n % i == 0:
      divisors.append(i)

  return sum(divisors)

for i in range(2, 10000):
  if d(i) not in amicable and i == d(d(i)) and d(i) != d(d(i)):
    amicable.append(i)
    amicable.append(d(i))

print sum(amicable)
