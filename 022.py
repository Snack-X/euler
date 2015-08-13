names = map(
  lambda s: s.replace("\"", ""),
  open("022.txt").read().split(",")
)

names.sort()

worth = map(
  lambda s: sum(
    map(
      lambda c: ord(c) - 64,
      list(s)
    )
  ),
  names
)

ans = sum([(i + 1) * v for i, v in enumerate(worth)])

print ans
