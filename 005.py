import euler

to = 20
ans = reduce(euler.lcm, range(1, to + 1))

print ans
