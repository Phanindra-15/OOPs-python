test_keys = ["phani", "sai", "yuvan"]
test_values = [21, 14, 5]


print ("original key list is : " + str(test_keys))
print ("original value list is : " + str(test_values))

res = {}
for key in test_keys:
	for value in test_values:
		res[key] = value
		
		break

print ("Resultant dictionary is : " + str(res))
