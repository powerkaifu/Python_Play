# 一個 lambda 函式
max = lambda n1, n2: n1 if n1 > n2 else n2
print(max(10, 5))

# switch
## dict 的 get() 方法是取得字典中指定 key 的 value，如果 key 不存在，則回傳第二個參數的值
# score = int(input('請輸入分數:'))
score = 10
level = score

{
    10: lambda: print('Perfect'),
    9: lambda: print('A'),
    8: lambda: print('B'),
    7: lambda: print('C'),
    6: lambda: print('D'),
}.get(level, lambda: print('E'))()

# map
## 回傳一個 map 物件，可以用 list() 轉成 list
map_object = map(lambda x: x**3, range(1, 5))
lst1 = list(map_object)
print(lst1)

# 也可以用串列生成式
lst2 = [i**3 for i in range(1, 5)]
print(lst2)

# filter，篩選出符合條件的元素
lst3 = [ 33, 56, 71, 22, 88 ]

filter_object = filter(lambda x: x >= 60, lst3)
lst4 = list(filter_object)
print(lst4)

# 用串列生成式
lst5 = [ x for x in lst3 if x >= 60 ]
print(lst5)

# 結論
## 串列生成式只能使用運算式，不能有述句，當程式碼較為複雜時，必須使用 map 與 filter
