start = 11
end = 25

for i in range(start, end+1):
	if i > 1:
		for j in range(3, i):
			if(i % j == 0):
				break
		else:
			print(i)

print('=======================')


start = 111
end = 129

for i in range(start, end+1):
	if i > 1:
		for j in range(2, i):
			if(i % j == 0):
				break
		else:
			print(i)

print('-------------------------------')
