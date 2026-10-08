import os
import openpyxl

excel_file = "students.xlsx"
new_excel_file = "new_students.xlsx"
from function_phu import *
if os.path.exists (excel_file):
    workbook = openpyxl.load_workbook(excel_file)
    worksheet = workbook.active

    if worksheet["F1"].value != "Tuổi":
        print("Có chạy")
        worksheet.insert_cols(6)
        worksheet["F1"] = "Tuổi"
    row_num = 2 
    for row_values in worksheet.iter_rows(
        min_row = 2, # bat dau doc tu hang 2
        values_only = True # chi lay gia tri cua cac o co gia tri
    ):
        print ("Nhập ngày sinh cho sinh viên", worksheet[f"A{row_num}"].value, worksheet[f"B{row_num}"].value, "(theo định dạng dd/mm/yyyy): ")
        ngay_sinh = input()
        tuoi = tinh_tuoi(ngay_sinh)
        worksheet[f"F{row_num}"] = tuoi
        row_num += 1
    
    workbook.save(excel_file)
    print("Đã lưu file thành công")
else:
    print("File không tồn tại")



