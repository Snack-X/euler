# sun = 0
# mon = 1
# sat = 6
day = 1
cnt = 0

def isLeap(y):
  if y % 4 != 0:
    return False
  elif y % 100 != 0:
    return True
  elif y % 400 != 0:
    return False
  else:
    return True


for year in range(1900, 2001):
  for month in range(1, 13):
    days = 0

    if day == 0 and year >= 1901:
      cnt += 1

    if month in (1, 3, 5, 7, 8, 10, 12):
      days = 31
    elif month in (4, 6, 9, 11):
      days = 30
    elif isLeap(year):
      days = 29
    else:
      days = 28

    day = (day + days) % 7

print cnt