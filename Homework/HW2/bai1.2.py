tuoi = int(input("Nhap tuoi: "))

if tuoi < 0:
    print("Dữ liệu không hợp lệ")
elif tuoi >= 0 and tuoi < 18:
    print("Chưa đủ tuổi")
else:
    print("Đủ tuổi")