n = 600851475143
i = 2
factors = []

while n > 1:
  while n % i == 0:
    factors.append(i)
    n /= i
  i += 1

print factors[-1]
