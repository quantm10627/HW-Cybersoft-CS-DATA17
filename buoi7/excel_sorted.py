# import openpyxl
# #1 Doc du lieu cua file excel
# workbook = openpyxl.load_workbook("new_vistor_data.xlsx")
# worksheet = workbook["Sheet1"]

# def bubble_sort(arr, column):
#     for i in range (len(arr)):
#         for j in range(0, len(arr)-i-1):
#             if arr[j][column] > arr[j+1][column]:
#                 arr[j][column] , arr[j+1][column]  = arr[j+1][column] , arr[j][column] 
# #2 Dua du lieu vao trong python
# data = []
# for row in worksheet.iter_rows(
#     min_row = 2,
#     values_only = True
# ):
#     data.append(list(row))

# #B3 : Sap xep du lieu
# data_sorted = bubble_sort(data, 6)

# #4 
# for row_index, row in enumerate (data_sorted, start=2):
#     for column_index, value in enumerate(row):
#         worksheet.cell(
#             row = row_index,
#             column=column_index,
#             value=value
#         )
# workbook.save("visitor.xlsx")
import openpyxl

def bubble_sort(data, column):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][column] > data[j+1][column]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

# Quy trình xử lý file excel
# B1: Đọc dữ liệu Excel
workbook = openpyxl.load_workbook("buoi8/visitor_data.xlsx")
worksheet = workbook["Sheet1"]

# B2: Đưa các hàng dữ liệu vào Python
data = []

for row in worksheet.iter_rows(
    min_row = 2,
    values_only = True
):
    data.append(list(row))

# B3: Sắp xếp dữ liệu theo Pricing Plan ID
sorted_data = bubble_sort(data, 6)

# B4: Ghi dữ liệu đã sắp xếp trở lại worksheet
for row_index, row in enumerate(sorted_data, start=2):
    for column_index, value in enumerate(row):
        worksheet.cell(
            row = row_index,
            column=column_index + 1,
            value=value
        )
# B5: Lưu thành file mới 
workbook.save("buoi8/visitor_data.xlsx")