def NextDay(d,m,y):
    # Ngày trong tháng
    ngaytrongthang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Kiểm tra năm nhuận
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        ngaytrongthang[1] = 29
    # Kiểm tra ngày hợp lệ
    if d < 1 or m < 1 or m > 12 or d > ngaytrongthang[m - 1]:
        return "Ngày không hợp lệ"
    # Tính ngày kế tiếp
    d += 1
    if d > ngaytrongthang[m - 1]:
        d = 1
        m += 1
        if m > 12:
            m = 1
            y += 1
    return f"Ngày kế tiếp là: {d}/{m}/{y}"
try: 
    d = (int(input("Nhập ngày: ")))
    m = (int(input("Nhap thang: ")))
    y = (int(input("Nhap nam: ")))
    print(NextDay(d,m,y))
except ValueError:
    print("Vui long nhap so nguyen")