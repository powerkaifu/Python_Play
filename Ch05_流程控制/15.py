n = int(input("請輸入一個數字："))

#(a)
"""
*****
****
***
**
*
"""

for row in range(n, 0, -1):
  for col in range(0, row):
    print('*', end = "")
  print("")

print("-" * 30)

#(b)
"""
    *
   **
  ***
 ****
*****
"""
for row in range(n, 0, -1):  # n=5，row=5, 4, 3, 2, 1
  for space in range(row - 1, 0, -1):
    print(' ', end = "")
  for col in range(n + 1 - row):
    print('*', end = "")
  print("")

print("-" * 30)

#(c)
"""
*****
 ****
  ***
   **
    *
"""
for row in range(n):  # n=5, 0,1,2,3,4
  for space in range(row):
    print(" ", end = "")
  for col in range(n - row, 0, -1):
    print("*", end = "")
  print("")

print("-" * 30)

#(d)
"""
*****
^****
^^***
^^^**
^^^^*
"""
for row in range(n):  # n=5, 0,1,2,3,4
  for space in range(row):
    print("^", end = "")
  for col in range(n - row, 0, -1):
    print("*", end = "")
  print("")

print("-" * 30)

#(e)
"""
1
12
123
1234
12345
"""
for row in range(1, n + 1):
  for col in range(1, row + 1):
    print(col, end = "")
  print("")

print("-" * 30)

#(f)
"""
5
54
543
5432
54321
"""
for row in range(1, n + 1):
  for col in range(1, row + 1):
    print(n + 1 - col, end = "")
  print("")

print("-" * 30)

#(g)
"""
1
22
333
4444
55555
"""
for row in range(1, n + 1):
  for col in range(1, row + 1):
    print(row, end = "")
  print("")

print("-" * 30)

#(h)
"""
0
12
345
6789
abcde
"""
count = 0
for row in range(1, n + 1):
  for col in range(1, row + 1):
    if (count < 10):
      print(count, end = "")
    else:
      print(chr(87 + count), end = "")  # chr() 將數字轉換成字元，chr(65) = 'A'，chr(97) = 'a'
    count = count + 1
  print("")

print("-" * 30)
