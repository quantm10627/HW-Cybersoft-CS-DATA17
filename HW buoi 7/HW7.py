import os
import openpyxl
#Yêu cầu 1. Nếu file đã có thì mở file cũ. Nếu chưa có thì tạo mới
excel_file = "students.xlsx" 
from function_phu import *
if os.path.exists (excel_file):
    workbook = openpyxl.load_workbook(excel_file)
    worksheet = workbook.active
else:
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.title = "Thông tin sinh viên"
    header =[
    "Mã sinh viên","Họ tên", "Lớp", "Email", "Số điện thoại"
]
    worksheet.append(header)
#Yêu cầu 2 và 3 nằm trong file function_phu.py
#Yêu cầu 5 nằm trong file hw7.YC5.py và hàm tính tuổi nằm trong file function_phu.py
while True: #Yêu cầu 4. Sau mỗi sinh viên hỏi: Bạn có muốn nhập tiếp ko? Y/N
    data_sv = []
    data_sv = Nhap_thongtin_sinhvien()
    worksheet.append(data_sv)
    kq = input("Tiếp tục nhập dữ liệu (Y/N): ")
    if kq == "N":
        break

workbook.save(excel_file)


