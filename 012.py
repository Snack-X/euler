def countDivisors(n):
  count = 0
  for i in range(1, int(n ** 0.5)):
    if n % i == 0:
      count += 1

  return count * 2

n = 1

while True:
  tri = (n * (n + 1)) / 2

  if countDivisors(tri) > 500:
    print tri
    break

  n += 1
