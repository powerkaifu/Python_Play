# 在大於１的自然數中，除了１和自己本身以外，沒有其他的正因 數的，稱為質數。


def isprime(x):
  if x < 2:
    return False
  for num in range(2, x):
    if (x % num == 0):
      return False
  return True


result = isprime(7)
print(result)
