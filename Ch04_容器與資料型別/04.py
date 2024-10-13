lst = [ 12, 43, 83, 91 ]
a = lst
a.append(23)

# a 與 lst 都指向同一個串列記憶體位址
print(lst)  # [12, 43, 83, 91, 23]

# copy() 是淺層複製，只會複製串列的第一層元素
lst = [ 12, 43, 83, 91 ]
a = lst.copy()  # 或者使用 a = lst[:]
a.append(23)

# a 與 lst 指向不同的串列記憶體位址
print(lst)  # [12, 43, 83, 91]
print(a)  # [12, 43, 83, 91, 23]
