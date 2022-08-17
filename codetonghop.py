# Hoàng Minh Ngọc VN05K65
from re import I
import sys
#Giới hạn limit đệ quy
sys.setrecursionlimit(1500)


def Extended_Euclid(a,b):
	if b == 0:
		return(a, 1, 0)
	else:
		d, x, y = Extended_Euclid(b,a%b)
		return(d, y, x - (a//b)*y)

def modun(a,b):
	if (b==0):
		return(a)
	else:
		d = modun(b,a%b)
		return(d)
#tính số dư 
def tinhUCLN(a,b):
	if b == 0:
		return(a, 1, 0)
	else:
		d, x, y = Extended_Euclid(b,a%b)
		return(d)

#nghịch đảo theo modun so a^-1 mod n 
def Mod_Inv(a, n):
	d, x, y = Extended_Euclid(a, n)
	b = x % n
	return(b)

# a^b mod n
# tính lũy thừa nhanh
def Mod_Exponentiation(a,b,n):
	if b == 0:
		return 1
	if b == 1:
		return a
	r = Mod_Exponentiation(a, b//2, n)
	r = (r*r)%n
	if b % 2 == 1:
		r = (r*a)%n
	return r%n

'''
for i in range(10,10000):
	x = i%120
	if ( x==1):
		print(i)
'''
#x = tinhUCLN(36,11)
#x = Mod_Inv(17, 113) 
#x = Mod_Exponentiation(3,36,19)
#print(x)

'''
for i in range(0,1000000):
	x = Mod_Exponentiation(3,i,19)
	# tính a^b mod n (3^i mod 19)
	if(x==4):
		print(i,":",x)
		break
'''

print("1) a^b mod n ")
print("2) a^-1 mod n ")
print("3) Tính Dlogarit x = Dlog(a,n)(b) <=> a^x mod n = b")
print("4) Tính UCLN của a và b ")
print("5) Tính số dư giữa 2 số a và b ")
print("6) Tinh DH_(a)(b,c) trong nhóm Z*n")
print("7) Tính các phần tử thuộc Z*n ")
print("8) Chữ kí số RSA ")
print("9) Chữ kí số ElGamal ")
print("Nhập chức năng ", end=' ')
c = int(input())
if(c==1):
	print("Nhập a ")
	a = int(input())
	print("Nhập b ")
	b = int(input())
	print("Nhập n ")
	n = int(input())
	s = Mod_Exponentiation(a,b,n)
	print("Gia tri cua ",a,"^",b," mod ", n ," = ", end=' ')
	print(s)

if (c==2):
	print("Nhập a ")
	a = int(input())
	print("Nhập n ")
	n = int(input())
	saa = Mod_Inv(a,n)
	print("Gia tri cua ",a,"^-1 mod",n, end = ' =  ')
	print(saa)

if (c==3): 
	print("Tính Dlogarit x = Dlog(a,n)(b) <=> a^x mod n = b ")
	print("Nhập a ")
	a = int(input())
	print("Nhập n ")
	n = int(input())
	print("Nhập b ")
	b = int(input())
	for i in range(0,1000000):
		x = Mod_Exponentiation(a,i,n)
		if (x==b):
			d = i
			break
	print("x = ", end = ' ')
	print(d)

if (c==4):
	print("Tính UCLN của 2 số a,b")
	print("Nhập số a ")
	a = int(input())
	print("Nhập số b ")
	b = int(input())
	s = tinhUCLN(a,b)
	print("UCLN cua (",a,",",b,") la : ", s)

if ( c==5 ): 
	print("Tính số dư của a chia cho n ")
	print("Nhập a ")
	a = int(input())
	print("Nhập n ")
	n = int(input())
	tg = 1
	s = Mod_Exponentiation(a,tg,n)
	print(a," mod ", n , " = ", s)
if(c==6):
	print("Tinh DH_(a)(b,c) trong nhóm Z*n")
	print("Nhập a: ")
	a = int(input())
	print("Nhập b: ")
	b = int(input())
	print("Nhập c: ")
	c = int(input())
	print("Nhập n: ")
	n = int(input())
	for i in range(0,100):
		if (Mod_Exponentiation(a,i,n) == b ):
			d1 = i
			break
	for i in range(0,100):
		if(Mod_Exponentiation(a,i,n) == c):
			d2 = i
			break
	print("x1 = ",d1,", x2 = ",d2)
	d = d1*d2
	s = Mod_Exponentiation(a,d,n)
	print("Giá trị cần tính là: ", end=' ')
	print(s)
if (c==7):
	print("Nhập Z*n với n = ", end = ' ')
	n = int(input())
	print("Các phần tử thuộc Z*n là : ", end = ' ')
	for i in range(1,n):
		if(tinhUCLN(i,n) == 1 ):
			x = tinhUCLN(i,n)
			print(i, end = ', ')
	print("Kiểm tra phần tử sinh ")
	print("Nhập phần tử muốn kiểm tra : ", end = ' ')
	a = int(input())
	for i in range(0,n):
		x = Mod_Exponentiation(a,i,n)
		print(x, end = ', ')
	
if(c==8):
	print("Hàm kiểm tra chữ kí  ")
	print("phi^e = m mod n")
	print("Nhập N ")
	n = int(input())
	print("Nhập e ")
	e = int(input())
	print("Nhập phi ")
	phi = int(input())
	m1 = Mod_Exponentiation(phi, e, n)
	print("Chữ kí : ",m1)
if(c==9):
	print("Chữ kí số ElGamal ")
	print("Nhập P ")
	p = int(input())
	print("Nhập g")
	g = int(input())
	print("Nhập d ")
	d = int(input())
	print("Nhập khóa tạm thời KE ")
	ke = int(input())
	print("Nhập thông điệp ")
	m = int(input())
	r = Mod_Exponentiation(g,ke,p)
	a2 = p-1
	a1 = (m-d*r)*Mod_Inv(ke,a2)
	print(" ta có mã s =  ", a1)
	print("Mã S khi chuyển sang mod  = ")
	a1 = int(input())
	s = Mod_Exponentiation(a1,1,a2) 
	print("Chữ kí số ElGamal (r,s) = (",r,",",s,")")

	



	

