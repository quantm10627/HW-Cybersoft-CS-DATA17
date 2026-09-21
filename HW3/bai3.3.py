number = input("Nhập danh sách số nguyên: ")
ds = number.split(",")
for i in range (len(ds)):
    ds[i] = int(ds[i])

nguong = int(input("Nhập ngưỡng giá trị: "))

Danhsach = []
for i in range (len(ds)):
    if ds[i] >= nguong:
        Danhsach.append(ds[i])
print(Danhsach)