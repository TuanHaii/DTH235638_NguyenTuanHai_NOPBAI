def docso(n):
    Donvi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    Chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi",
            "bảy mươi", "tám mươi", "chín mươi"]
    if n < 10:
        dv = Donvi[n]
        dvMoi = dv[0:1].upper() + dv[1:]
        return dvMoi
    elif n < 20:
        if n == 10:
            return "mười"
        elif n == 15:
            return "mười lăm"
    # n//10 để lấy hàng chục, n%10 để lấy hàng đơn vị
    else:
        chuc =   n // 10
        chucMoi = Chuc[chuc][0:1].upper() + Chuc[chuc][1:]
        donvi =  n % 10
        if n == 0:
            return chucMoi
        elif donvi == 5:
            return chucMoi + " lăm"
        else:
            return chucMoi + " " + Donvi[donvi]
try:
    n = int(input("Mời nhập vào số tối đa có 2 chữ số:"))
    if 0 <= n < 100:
        print(docso(n))
    else:
        print("Số không hợp lệ")    
except ValueError:
    print("Vui lòng nhập số nguyên")