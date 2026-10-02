toan = float(input("Nhap diem toan: "))
van = float(input("Nhap diem van: "))
anh = float(input("Nhap diem anh: "))
diemtb = (toan + van + anh) / 3
print("Diem trung binh: ", round(diemtb, 2))

if diemtb >= 8:
    print("Hoc sinh gioi")
elif diemtb >= 6.5 and diemtb < 8:
    print ("Hoc sinh kha")
else:
    print("Hoc sinh trung binh")