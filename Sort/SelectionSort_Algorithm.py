#

arr = [2,6,3,8,1,9]

# Duyet den cuoi mang
for i in range(len(arr)):
	# Dat vi tri cua phan tu dau tien la nho nhat
	min_index = i
	#Duyet phan tu tiep theo trong mang den het mang
	for j in range(i+1, len(arr)):
		#Kiem tra phan tu tiep theo nay voi phan tu cua vi tri set dau tien neu nho hon
		if arr[j] < arr[min_index]:
			# Set phan tu hien tai list indices must be integers or slices, not floatthanh phan tu nho nhat va tiep tuc kiem tra den cuoi mang
			min_index = j
	# Swap lai vi tri 2 phan tu cua j va phan tu dau tien
	arr[i],arr[min_index] = arr[min_index],arr[i]

for x in range(len(arr)):
	print(arr[x])

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
selection_sort(arr)
