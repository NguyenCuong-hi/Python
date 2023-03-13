
arr = [5,3,1,6,7]

# duyet mang voi index = 1
for i in range(1, len(arr)):
	# Set value cho phan tu hien tai 
	sorted_index = arr[i]
	print('sorted_index: ',sorted_index)
	#Duyet mang tu index = 0
	j = i-1
	print('j=',j)
	#Kiem tra dieu kien neu arr[i] < arr[j] thi doi cho hien tai ve ben phai
	while j>= 0 and sorted_index < arr[j]:
		arr[j + 1] = arr[j]
		j = j-1
	arr[j + 1] = sorted_index

for i in range(0,len(arr)):
	print(arr[i])

