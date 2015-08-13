import euler

print sum(
  filter(
    lambda n: n % 2 == 0,
    euler.fibonacci_to_n(4000000)
  )
)
