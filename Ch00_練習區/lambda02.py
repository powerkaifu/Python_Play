from functools import reduce

# 題目 1：基本運算
my_sum = lambda x, y: x + y
print(my_sum(1, 2))

# 題目 2：平方數
my_square = lambda x: x**2
print(my_square(3))

# 題目 3：過濾偶數
lst = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
filter_obj = filter(lambda x: x % 2 == 0, lst)
lst2 = list(filter_obj)
print(lst2)

# 題目 4：字符串長度排序
lst = [ 'Tom', 'John', 'Florencia', 'Shelly', 'Roger']
sorted_lst = sorted(lst, key = lambda x: len(x))
print(sorted_lst)

# 題目 5：映射平方
lst = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
map_obj = map(lambda x: x**2, lst)
print(list(map_obj))

# 題目 6：條件表達式
even_or_odd = lambda x: '偶數' if x % 2 == 0 else '奇數'
print(even_or_odd(10))

# 題目 7：計算列表中每個元素的平方和
lst = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
square_num = reduce(lambda acc, x: acc + x**2, lst, 0)
print(square_num)

# 題目 8：合併兩個列表
lst1 = [ 1, 2, 3 ]
lst2 = [ 4, 5, 6 ]
combine = lambda a, b: a + b
print(combine(lst1, lst2))

# 題目 9：過濾大於 5 的數字
lst = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
result = list(filter(lambda x: x > 5, lst))
print(result)

# 題目 10：計算字符串長度
word_len = lambda x: len(x)
print(word_len('KaiFu'))

# 題目 11：最大值，寫一個 lambda 函數，讓它接收三個數字，並返回最大值。
my_max = lambda a, b, c: max(a, b, c)
print(my_max(3, 10, 11))

# 題目 12：自訂鍵的排序
lst = [
    ( "Alice", 25 ),
    ( "Bob", 22 ),
    ( "Charlie", 30 ),
]

result = sorted(lst, key = lambda x: x[1])
print(result)

# 嵌套 map() 和 filter()
## 給定一個數字列表，使用 lambda 結合 filter() 篩選出偶數，並使用 map() 將它們的值加倍。

lst = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
result = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, lst)))
print(result)

## 也可以用串列生成式達成
result = [x * 2 for x in lst if x % 2 == 0]
print(result)
"""
串列生成式：結構清楚，適合簡單的邏輯判斷和轉換，Pythonic（符合 Python 習慣）。
map() / filter()：適合運用高階函數風格，尤其在搭配 lambda 函數時表現優秀。

串列生成式較直觀，適合初學者或希望程式碼可讀性高的情境。
map() / filter() 讓你的程式風格更加函數式，對熟悉高階函數概念的人來說較為自然。
"""
