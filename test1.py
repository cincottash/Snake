myList = []

myList.append([0, 0])
myList.append([1, 1])

for item in myList:
	print(item)
print("#########")
myList.insert(0, [2, 2])

for item in myList:
	print(item)