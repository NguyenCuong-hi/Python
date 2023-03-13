#Sort Algorithm 

arrays = [14,33,27,35,10]

# print(arrays)
# print(max(arrays))
# print(min(arrays))
# print(len(arrays))
def bubble_sort(arr):
    n = len(arr)
    # Lặp qua tất cả các phần tử của mảng
    for i in range(n):
        # Lặp qua các phần tử còn lại của mảng
        for j in range(0, n-i-1):
            # So sánh phần tử hiện tại với phần tử tiếp theo
            if arr[j] > arr[j+1]:
                # Hoán đổi chỗ các phần tử nếu chúng không ở đúng thứ tự
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Giai thuat : 14,33,27,35,10

 # i = 0; j=0 : 14 33

for i in range(len(arrays)):
	
	for j in range(0,len(arrays)-i-1):
		print('i=', i ,'->',len(arrays), ' ,j = ', j ,'->' ,len(arrays)-i-1, arrays[i] , arrays[j],'' )
		if arrays[j] > arrays[j + 1]:
			print(arrays[j], arrays[j+1])
			arrays[j], arrays[j+1] = arrays[j+1], arrays[j]

for i in range(len(arrays)):
	print(arrays[i])
