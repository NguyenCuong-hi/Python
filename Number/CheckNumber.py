# So nguyen to : So co uoc la 1 va chinh no 2,3,5,7
import math
def songuyento(a):
	if a < 2:
		return False
	for i in range(2,int (math.sqrt(a)) + 1):
		if a % i == 0:
			return False
	return True

for i in range(0,10):
	if songuyento(i):
		print(i)

# So hoan hao: So co tong cac uoc cua no bang chinh no	
def sohoanhao(a):
	tong = 0;
	for i in range(1,a):
		if a % i == 0:
			tong+= i
	if tong == a:
		return True
	return False

# So chinh phuong la so co can bac 2 la 1 so nguyen 
def sochinhphuong(a):
	number = int (math.sqrt(a))
	for i in range(1,a):
		if number % 2 == 0:
			return True
	return False

print(sochinhphuong(5))

# Uoc chung lon nhat cua 2 so: uocchung(6,8) = uocchung(8,6%8) = uocchung(8,2) = uocchung(2,2%8)= uocchung(2,0)
# Uoc chung la so ma deu la uoc cua 2 so
def uocchung(a,b):
	if b == 0:
		return a
	return uocchung(b, a%b)

# boichung(6,8) = 6 * 8 / 2 = 16
# boi chung nho nhat la  tich cua 2 so co uoc la nho nhat
def boichung(a,b):
	return int ((a * b)/uocchung(a,b))

# So thuan nghich : cac so co dang 123321
def sothuannghich():
	a = []
	i, dem = 0
	while n >= 0:
		a[dem + 1] = n % 10
		n = n / 10
	for i in range(0, dem/2):
		if a[i] != a[dem - i -1]:
			return False
	return True


def fibonacy_one(a):
	if a < 0:
		return -1
	elif a ==0 or a== 1:
		return 1
	else:
		return fibonacy_one(a- 1) + fibonacy_one(a-2)
def fibonacy_two(a,b, n):
	if n <= 2:
		return False
	if n > 2:
		for  i in range(2,n):
			f = a + b
			a = b
			b = f
def fibonanci_three( a,b,c,index):
	if index<= 2:
		return 0
	if index > 2:
		for i in range(2,index):
			f = a + b + c
			a = b
			b = c
			c = f
	return f
print('fibonanci_three ', fibonanci_three(1,2,3,3))