MAX = 1000000
count = [False] * MAX
count[0] = 0
count[1] = 1

for i in range(2, MAX):
  length = 0
  n = i

  while n != 1:
    if n % 2 == 0:
      n = n / 2
    else:
      n = 3 * n + 1

    length += 1

    if n < MAX and count[n] != False:
        count[i] = length + count[n]
        break

maxlen = max(count)
print count.index(maxlen), maxlen
