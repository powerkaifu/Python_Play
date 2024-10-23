# 設計 primes(x) 函數，可以找出小於等於 x 的所有質數，將找出的質數以串列形式傳回


def isprimes(n):
  if n < 2:
    return False
  for num in range(2, n):
    if n % num == 0:
      return False
  return True


def primes(x):
  return [ i for i in range(2, x) if isprimes(i) ]


list_prime = primes(13)
print(list_prime)
