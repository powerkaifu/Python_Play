# (a) 建立字典 d1， { 'Jan':None, 'Feb':None, 'Mar':None }
lst = [ 'Jan', 'Feb', 'Mar']
d1 = dict.fromkeys(lst)
print(d1)

# (b)
d1['Jan'] = 1
d1['Feb'] = 2
d1['Mar'] = 3

print(d1)

# (c)
d1.update({ 'Apr': 4})
print(d1)

# (d)
d1.pop('Feb')
print(d1)
