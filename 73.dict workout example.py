c=dict()
line='my name is phani and my name is sumanth and my goal is to become a software officer and my goal is to be a good student in all the academics while coming to my academicsi am sis are of sis name my'
words=line.split()
print(words)


for word in words:
    c[word]=c.get(word,0)+1
print(c)
