c=dict()

names=['a','b','c','d','e','a']

for name in names:
    if name not in c:
        c[name]=1
    else:
        c[name]=c[name]+1
print(c)
