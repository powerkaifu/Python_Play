# range() 建立 1~20 奇數組合而成的串列

r1 = range(1, 20, 2)
print(list(r1))

# str1 = 'machineLearning'，建立 str1 的字串串列

str1 = 'machineLearning'
str1_list = list(str1)
print(str1_list)

# 試利用 range() 建立以下
## (a) [100, 104, 108, 112, 116, 120]
list_a = list(range(100, 121, 2))
print(list_a)

## (b) [-1, -2, -3, -4, -5, -6, -7, -8, -9]
list_b = list(range(-1, -10, -1))
print(list_b)

## (c) [-1, -4, -7, -10, -13, -16, -19]
list_c = list(range(-1, -20, -3))
print(list_c)

## (d) [10, 19, 28, 37, 47, 55, 64]
list_d = list(range(10, 65, 9))
print(list_d)
