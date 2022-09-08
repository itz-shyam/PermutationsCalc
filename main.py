n = int(input("N value: "))
r = int(input("R Value: "))


def factorial(a):
  if a == 0:
    return 1
  else:
    return a * factorial(n - 1)
nf = factorial(n)
bf = factorial(r)
perm=nf/factorial(n-r)
print(perm)
