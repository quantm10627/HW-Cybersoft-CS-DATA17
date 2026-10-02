salary = 15
bonus = 0.1
KPI = 100

sale = float(input("Nhap doanh thu : "))

if sale >= 100:
    salary*=1.1
elif sale < 80 and sale >= 10:
    salary *= 0.9
print ("Luong thuc nhan duoc: ", salary)