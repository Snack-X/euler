ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teen = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def getSpokenNumber(n):
  if n < 10:
    return ones[n]

  elif n > 10 and n < 20:
    return teen[n - 10]

  elif n < 100:
    if n % 10 == 0:
      return tens[n / 10]
    else:
      return tens[n // 10] + ones[n % 10]

  elif n < 1000:
    return ones[n // 100] + "hundred" + (("and" + getSpokenNumber(n % 100)) if n % 100 != 0 else "")

  elif n < 1000000:
    return getSpokenNumber(n // 1000) + "thousand" + (("and" + getSpokenNumber(n % 1000)) if n % 1000 != 0 else "")

  else:
    return "?"

total = sum(len(getSpokenNumber(i)) for i in range(1, 1001))

print total
