# [] 或 list() 建立串列
# 串列具有 mutable(可變可修改)、ordered(有序)、index(索引)、duplicate(重複) 的特性

# range() 不包含結束值
r1 = range(0, 10)  # 0 ~ 9
value1 = r1[-1]  # 9，取得最後一個元素
value2 = r1[3 : 7]  # [3, 4, 5, 6]，取得索引 3 ~ 6 的元素
## range(0, 9, 0.5) # range 不支援浮點數

# list() 建立串列
list1 = list(range(1, 6))  # [1, 2, 3, 4, 5]
list2 = list(range(1, 10, 2))  # [1, 3, 5, 7, 9]
list3 = list(range(20, 6, -2))  # [20, 18, 16, 14, 12, 10, 8]
list4 = list('Python')  # ['P', 'y', 't', 'h', 'o', 'n']
str1 = ''.join(list4)  # 'Python'
print(str1)

# []
list10 = [ 5, 8, 4 ]  # [5, 8, 4]
list11 = list([ 2, 3, 7 ])  # [2, 3, 7]

# len() 取得串列長度
list20 = [ 1, 3, 5, 7, 9 ]
len(list20)  # 5

# max() 取得串列最大值
max(list20)  # 9

# min() 取得串列最小值
min(list20)  # 1

# sum() 取得串列總和
sum(list20)  # 25

# 串列合併
list('abc') + list20  # ['a', 'b', 'c', 1, 3, 5, 7, 9]

# 重複串列
[ 1, 2, 3 ] * 3  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 比較串列
[ 1, 2, 3 ] == [ 1, 2, 3 ]  # True
[ 1, 2, 3 ] == [ 1, 3, 2 ]  # False
[ 1, 2, 3 ] > [ 1, 1, 4 ]  # True
[ 'a', 'b', 'c'] > [ 'a', 'a', 'd']  # True
[ 'a', 'b', 'c'] > [ 'a', 'a', 5 ]  # TypeError: 不支援不同型別比較

# in

3 in range(0, 10)  # True
[ 1, 3 ] in [ 1, 2, 3, 4, 5 ]  # False，[1,3] 並不是後者的子集合
[ 1, 3 ] in [[ 1, 3 ], 4, 5]  # True
3 in [ 1, 2, 3, 4, 5 ]  # True
[3] in [ 1, 2, 3, 4, 5 ]  # False，[3] 並不是後者的子集合
'python' in [ 'Learning', 'python']  # True
'python' in ['Learning python']  # False，'python' 並不是後者的子集合

# 串列與切片

list30 = [ 7, 9, 11, 8, 17 ]
list30[0 : 4 : 2]  # [7, 11]，取得索引 0 ~ 3 的元素，間隔 2
list30[2 :]  # [11, 8, 17]，取得索引 2 之後的元素
list30[: 4]  # [7, 9, 11, 8]，取得索引 0 ~ 3 的元素
list30[:-2]  # [7, 9, 11]，取得索引 0 ~ -3 的元素，不包含倒數第二個元素

# del 刪除串列元素
del list30[-1]  # [7, 9, 11, 8]，刪除最後一個元素
del list30[1 :]  # [7]，刪除索引 1 之後的元素
del list30[:]  # []，刪除所有元素，清空串列裡面的元素
del list30  # 從記憶體中刪除串列
# print(list30)  # NameError: name 'list30' is not defined

# lst.append() 新增元素到串列尾端
lst = []
lst.append('apple')
lst.append('banana')
lst.append('orange')
lst.append('apple')  # ['apple', 'banana', 'orange', 'apple']

# lst.extend() 將串列合併
lst2 = [ 3, 6, 8, 10 ]
# lst2.append([ 10, 20 ])  # [3, 6, 8, 10, [10, 20]]，將串列當成一個元素加入串列
## 使用 extend() 會將串列元素合併
lst2.extend([ 10, 20 ])  # [3, 6, 8, 10, 10, 20]

# lst.remove() 移除串列中第一個符合的元素
lst.remove('apple')  # ['banana', 'orange', 'apple']

# lst.index() 取得串列中第一個符合的元素索引
lst.index('orange')  # 1

# lst.insert(index, obj) 插入元素到指定索引
lst.insert(1, '哈囉')  # ['banana', '哈囉', 'orange', 'apple'] 在索引 1 插入 '哈囉'

# lst.pop() 移除串列最後一個元素
# lst.pop(index) 移除串列指定索引元素
a = lst.pop()  # ['banana', '哈囉', 'orange'] 移除最後一個元素，並回傳移除的元素
print(a)  # apple
b = lst.pop(1)  # ['banana', 'orange'] 移除索引 1 的元素
print(b)  # 哈囉

lst.append('grape')
lst.append('grape')

# lst.count() 計算串列中元素出現次數
lst.count('grape')  # 2

# lst.sort() 排序串列
lst2 = [ 10, 40, 20, 30, 90, 60 ]
lst2.sort()  # [10, 20, 30, 40, 60, 90]，預設由小到大排序
print(lst2)

# lst.sort(reverse = True) 由大到小排序
lst2.sort(reverse = True)  # [90, 60, 40, 30, 20, 10]，由大到小排序
print(lst2)

# lst.reverse() 反向排列
lst2.reverse()  # [10, 20, 30, 40, 60, 90]，反轉串列
print(lst2)

# lst.clear() 清空串列
lst.clear()  # []，清空串列

# lst.copy() 複製串列
origin = [ 1, 2, 3, 4, 5 ]
copy = origin.copy()

print(copy)  # [1, 2, 3, 4, 5]
copy[0] = 10
print('origin', origin)  # [1, 2, 3, 4, 5]
print('copy', copy)  # [10, 2, 3, 4, 5]，不會影響原始串列

## copy() 是淺拷貝，只會複製第一層的元素，如果串列中有串列，則只會複製串列的參考

origin2 = [
    {
        'name': 'John', 'age': 20
    },
    {
        'name': 'Mary', 'age': 30
    },
]
copy2 = origin2.copy()
print(copy2)  # [{'name': 'John', 'age': 20}, {'name': 'Mary', 'age': 30}]

copy2[0]['name'] = 'Python'

print('origin2', origin2)  # [{'name': 'Python', 'age': 20}, {'name': 'Mary', 'age': 30}]
## copy2 修改串列中的元素，原始串列也會被修改，因為串列中的元素是參考
print('copy2', copy2)  # [{'name': 'Python', 'age': 20}, {'name': 'Mary', 'age': 30}]

# 巢狀串列
grades = [
    [ 67, 80, 87, 69 ],
    [ 71, 80, 65, 53 ],
    [ 77, 58, 60, 49 ],
]

## 生成式
firstGrage = [grade[0] for grade in grades]
print(firstGrage)  # [67, 80, 87, 69]
