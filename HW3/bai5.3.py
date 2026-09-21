number = input("Nhập danh sách số nguyên: ")
ds = number.split(",")
for i in range (len(ds)):
    ds[i] = int(ds[i])

x = int (input("Nhập số nguyên cần tìm: "))
vi_tri =[]
for i in range (len(ds)):
    if ds[i] == x:
        vi_tri.append(i)
if len(vi_tri) == 0:
    print("Không tìm thấy")
else:
    print("Vị trí các phần tử cần tìm: ", vi_tri)