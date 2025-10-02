x=int(input("Nhập x:"))
n=int(input("Nhập N:"))
def GiaiThuaN(n):
    if n <= 1:
        return 1
    return n * GiaiThuaN(n-1)
def Mu(x, i):
    return x ** i

def TinhDaySo(x, n):
    s = 0
    for i in range(1, n+1):
        s += Mu(x, i) / GiaiThuaN(i)
    return s

print("Kết quả dãy số là:",TinhDaySo(x,n))     
# x=int(input("Nhập x:"))
# n=int(input("Nhập N:"))
# s=0
# for i in range(1,n+1):
#  tu=x**i
#  mau=1
#  for j in range(1,i+1):
#      mau=mau*j
#  s=s+(tu/mau)
# print("s({0},{1})={2}".format(x,n,s))