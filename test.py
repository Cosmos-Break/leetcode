a = [1,2,3]
b = []
b.append(a[:])
print(b)
a[0] = 2
print(b)