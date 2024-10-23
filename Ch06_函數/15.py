def find_int(num = 3):
  if num % 2 == 0:
    num = num - 1
  if (num - 1) % 4 == 0:
    return num - 3
  else:
    return num - 1


print(find_int(11))
