#
arr = [12,5,2,66,3]

def quicksort(arr, left, right):
	#Dat moc la trung binh cua day so
	middle = (int)(left + ((right - left)/2))
	pivot = arr[middle]
	# i duyet ben trai
	# j duyet ben phai
	i = left
	j = right
	#Neu trai < phai
	while left < right:
		# Duyet ben trai neu phan tu ben trai nho hon moc
		while arr[i] < pivot:
			i = i + 1
			print(pivot)
		# Duyet ben phai neu phan tu ben phai lon hon moc
		while arr[i] > pivot:
			j = j - 1
		#Neu cac phan tu duoc duyet ben trai nho hon ben phai, thuc hien doi cho
		if i <= j:
			a[i],a[i] = a[j],a[j]

			i = i+ 1
			j = j-1
		if left < j:
			quicksort(arr,left,j)
		if right > i:
			quicksort(arr,i,right)
left = 0
right = len(arr) - 1

quicksort(arr,left,right)
for i in range(len(arr)):
	print(arr[i])