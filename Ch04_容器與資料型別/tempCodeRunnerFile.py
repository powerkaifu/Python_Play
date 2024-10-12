# (a)
lst = [ 43, 12, 12, 34 ]
lst.extend([ 2, 12 ])
print(lst)  # [43, 12, 12, 34, 2, 12]
print(lst.count(12))  # 3

# (b)
lst = [ 43, 12, 12, 34 ]
lst.append([ 25, 99 ])
print(lst)

# (c)
lst = [ 43, 12, 12, 34 ]
lst.insert(2, 65)
print(lst)
