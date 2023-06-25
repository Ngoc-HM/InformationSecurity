#Hoàng Minh Ngọc Việt Nhật 05 K65
import sys
#Giới hạn limit đệ quy
sys.setrecursionlimit(1500)
def Extended_Euclid(a,b):
	if b == 0:
		return(a, 1, 0)
	else:
		d, x, y = Extended_Euclid(b,a%b)
		return(d, y, x - (a//b)*y)

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

# a = 779
#b = 279997
#n = 11413
#x = tinhUCLN(21,15)
#x = Mod_Inv(16, 113)
#x = Mod_Exponentiation(a,b,n)
#print(x)
print("---HE MAT MA RSA---")
print("Nhập P: ")
p = int(input())
print("Nhập Q: ")
q = int(input())
print("Nhập e: ")
e = int(input())
N = p*q
tg = (p-1)*(q-1)
for i in range(1,100000):
	if((i*e)%tg == 1):
		d=i
		break

print("Key d: ")
print(d)
print("1) Giải Mã")
print("2) Mã Hóa")
chuongtrinh = int(input())
if(chuongtrinh==1):
	print("Chương trình giải mã khởi động !")
	print("Nhập bản mã cần giải: ")
	c = int(input())
	m = Mod_Exponentiation(c,d,N)
	print("Bản rõ là : ")
	print(m)
if(chuongtrinh==2):
	print("Chương trình mã hóa khởi động!")
	print("Nhập bản rõ: ")
	m = int(input())
	c = Mod_Exponentiation(m,e,N)
	print("Bản mã hóa là: ")
	print(c)






