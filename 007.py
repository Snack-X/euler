count = 0
prime = []
num = 1

def isPrime(n):
  for i in prime:
    if n % i == 0:
      return False
  return True

while count < 10001:
  num += 1
  if isPrime(num):
    prime.append(num)
    count += 1

print prime[-1]
