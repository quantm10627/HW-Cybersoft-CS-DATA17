import openpyxl
import os
excel_file = "user_information.xlsx"
from ham_phu import *
# 3 bước tạo file excel:  tạo workbook, lấy worksheet, đặt tên worksheet
if os.path.exists (excel_file):
    workbook = openpyxl.load_workbook(excel_file)
    worksheet = workbook.active
else:
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.title = "Thông tin người dùng"

#Lưu thông tin 5 user
headers = [
    "Họ và tên", 
    "Ngày sinh",
    "Email",
    "Số điện thoại",
    "Công việc"
]
worksheet.append(headers)
while True:
    ho_ten = input("Nhập họ và tên:")
    ngay_sinh = input ("Nhập ngày sinh:")

    # Kiem tra nhap email hop le
    while True:
        email = input("Nhập email:")
        dinh_dang_email_dung = validate_email(email)
        if dinh_dang_email_dung:
            break
        else:
            print("Email khong hop le. Vui long nhap lai")


    # Kiem tra so dien thoai hop le
    while True:
            sdt = input("Nhập số điện thoại:")
            dinh_dang_sdt_dung = validate_phone(sdt)
            if dinh_dang_sdt_dung:
                break
            else:
                print("So dien thoai khong hop le. Vui long nhap lai")


    job = input("Nhập công việc: ")

    #Data của user
    user_data = [ho_ten, ngay_sinh, email, sdt, job]
    worksheet.append(user_data)
    workbook.save(excel_file)
    kq = int(input("Bạn muốn tiếp tục không(1/0):"))
    if kq == 0:
        break