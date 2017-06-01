s = sorted([36, 5, -12, 9, -21])
print(s)
# 按绝对值大小排序
s2 = sorted([36, 5, -12, 9, -21], key=abs)
print(s2)

s3 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(s3)

s4 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(s4)
