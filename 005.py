from fractions import gcd

to = 20

def lcm(a, b):
  return a * b // gcd(a, b)

ans = reduce(lcm, range(1, to + 1))

print ans
