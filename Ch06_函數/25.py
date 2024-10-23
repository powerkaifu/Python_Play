#(1)
def sign(x):
  return 1 if x >= 0 else -1


print(sign(10))

#(2) lambda
sign_lambda = lambda x: 1 if x >= 0 else -1
print(sign_lambda(10))

#(c)
lst = [ 9, -3, 8, 2, 1, -1, -4 ]

result = list(map(sign_lambda, lst))

print(result)

#(d)
sign2 = lambda x: 1 if x > 0 else 0 if x == 0 else -1

print(sign2(10))  # 1
print(sign2(0))  # 0
print(sign2(-5))  # -1
