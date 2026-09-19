luong = 15000000
KPI = 100000000
sale = int (input("Nhap doanh thu: "))

if sale >= KPI:
    luong*=1.1
elif sale <= 80000000:
    luong*=0.9
else:
    print ("Khong duoc tang luong")
print ("Luong thuc nhan:", luong)