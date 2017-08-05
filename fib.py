def fibsum(n):
  a, b = 1, 2
  i = 1
  while i < n:
    print(a, end=' ')
    i = i + 1
    a, b = b, a + b + 1
  print()
  print(a/2)
fibsum(33)