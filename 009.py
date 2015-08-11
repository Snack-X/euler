import math

for a in range(1, 1000):
  for b in range(1, 1000):
    c = a * a + b * b
    ceil = math.ceil(c ** 0.5)
    floor = math.floor(c ** 0.5)

    if ceil == floor and a + b + ceil == 1000:
      print a * b * ceil