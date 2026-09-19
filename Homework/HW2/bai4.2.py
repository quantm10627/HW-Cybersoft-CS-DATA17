luong = 15000000
sale = float(input("Nhập doanh thu: "))

if sale > 100000000:
    luong*=1.1
elif sale >= 10000000 and sale <=80000000:
    luong*=0.9
elif sale < 10000000:
    print("Cần xử lý theo quy định doanh nghiệp")
print("Lương thực nhận: ", luong)