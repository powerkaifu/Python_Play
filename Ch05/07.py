#(a)
print('5為奇數') if 5 % 2 == 1 else print('5為偶數')

#(b)
x, y = 6, 3
z = x if x > y else y
print(z)

#(c)
x = [ 5, 6, 4 ]
print('x is not empty') if x else print('x is empty')

#(d)
x = -10
x = -x if x < 0 else x
print(x)
