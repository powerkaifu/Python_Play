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

# (d)
lst = [ 43, 12, 12, 34 ]
lst.remove(12)
lst.remove(12)
print(lst)

lst2 = list(filter(lambda x: x != 12, lst))
print(lst2)

lst3 = [ x for x in lst if x != 12 ]
print(lst3)

# (e)
lst = [ 43, 12, 12, 34 ]
lst.sort(reverse = True)
print(lst)

# (f)
lst = [ 43, 12, 12, 34 ]
lst.pop()
print(lst)
lst.pop(2)
print(lst)
