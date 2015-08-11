prime = []

def isPrime(n):
  for i in prime:
    if n % i == 0:
      return False
  return True

for num in range(2, 2000000):
  if isPrime(num):
    prime.append(num)

print sum(prime)
