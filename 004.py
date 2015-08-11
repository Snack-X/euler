ans = 1

for a in range(100, 1000):
  for b in range(100, 1000):
    c = a * b
    strC = str(c)
    revC = strC[::-1]

    if strC == revC and ans < c:
      ans = c

print ans
