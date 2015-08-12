print sum(
  map(
    int,
    list(
      str(
        reduce(
          lambda a, b: a * b,
          range(1, 101)
        )
      )
    )
  )
)
