# 設 lst = [9, 8, 7, 1, 2, 3, 7, 3, 2]

lst = [ 9, 8, 7, 1, 2, 3, 7, 3, 2 ]

## (a) 取出 lst 中，索引為 0 ~ 2 的元素(包含 2)

list_a = lst[0 : 3]
print(list_a)

## (b) 取出 lst 最後 3 個元素
list_b_1 = lst[-1 :-4 :-1]  # 倒過來取
list_b_2 = lst[len(lst) - 3 :]  # 按照索引取
print(list_b_1)
print(list_b_2)

## (c) 取出 lst 中，索引為 4 到 7 的元素

list_c = lst[4 : 8]
print(list_c)

## (d) 取出索引偶數的元素
list_d = lst[2 :: 2]
print(list_d)

## (e) 找出 lst 的長度、最大值、最小值，並計算元素總和
print(len(lst))  # 9
print(max(lst))  # 9
print(min(lst))  # 1
print(sum(lst))  # 42

## (f) 反向提取倒數第 1 個到倒數第 4 個元素 [2,3,7,3]
print(lst[-1 :-5 :-1])

## (g) 將 lst 反向排列，結果為 [2,3,7,3,2,1,7,8,9]
lst.reverse()
print(lst)  # 反向排列

lst.sort()  # 由小到大排序
print(lst)

lst.sort(reverse = True)  # 由大到小排序
print(lst)
