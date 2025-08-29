import math

try:
    r = float(input("Nhập bán kính hình tròn: "))
    cv = 2 * math.pi * r
    print("Chu vi hình tròn là:", cv)
except ValueError:
    print("Giá trị nhập vào không hợp lệ.")