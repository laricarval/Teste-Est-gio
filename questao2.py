def a(n):
  if n in {0, 1}:  # Base case
    return n
  return a(n - 1) + a(n - 2)

teste = [a(n) for n in range(15)]
print (teste)