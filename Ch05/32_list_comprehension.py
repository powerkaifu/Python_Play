# 串列生成式公式：[運算式 for 項目 in 可迭代項目 if 條件式]
## 前面的 if 是處理項目的條件，被篩選出來的項目才會被運算式處理
## 後面的 if 是過濾項目，只有符合條件的項目才會在運算市中被處理，如果都沒寫，則所有項目都會被處理

#(a) 建立一個 1 到 10 的平方數列表

a = list(x**2 for x in range(1, 11))
print(a)

#(b) 建立一個 1 到 50 之間，可以同時被 3 和 4 整除的串列

b = list(x for x in range(1, 51) if x % 3 == 0 and x % 4 == 0)
print(b)

#(c) 取出字串 'List comprehension' 中所有的母音，並組成一個字元串列

check_word = 'aeiouAEIOU'
result = list(char for char in 'List comprehension' if char in check_word)

print(result)

#(d) 依串列 [3, -1, 4, 7, -3, 2] 的值來建立另一個新串列，若串列元素為正，則新串列元素的值為 1，否則為 -1
# 答案為 [1, -1, 1, 1, -1, 1]

d = list(1 if x > 0 else -1 for x in [ 3, -1, 4, 7, -3, 2 ])
print(d)
