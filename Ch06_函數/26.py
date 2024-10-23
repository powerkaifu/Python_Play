# 改成 lambda
#(1)
f1 = lambda x: x if x > 0 else -x

#(2)
f2 = lambda x: True if x % 2 == 0 else False

#(c)
lst = [ 1, 2, 3, 4, 5 ]
f3 = lambda lst: sum([i**2 for i in lst])
result = f3(lst)
print(result)

#(d)
lst = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
f4 = lambda lst: [ i for i in lst if i % 2 == 0 ]
result = f4(lst)
print(result)
