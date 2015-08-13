import euler

n = 1

while True:
  tri = (n * (n + 1)) / 2

  if euler.divisors_count(tri) > 500:
    print tri
    break

  n += 1
