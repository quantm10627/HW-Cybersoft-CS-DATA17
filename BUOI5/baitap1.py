# tạo một dictionary sản phẩm gồm mã sp, tên, giá, sl
# sau đó in ra tên, đổi giá, thêm category, xóa số lượng

sanpham ={
    "ten" : ["sp1", "sp2", "sp3"],
    "ma_sp" : ["01", "02", "03"],
    "gia" : [100, 200, 300],
    "soluong" : [1,2,3]
}
# YC1
def print_name (sanpham):
    for i in range(len(sanpham["ten"])):
        print (sanpham["ten"][i])
print_name(sanpham)

# YC2
# def change_cost (sanpham):
#     name = input("Nhập tên sản phẩm muốn đổi giá: ")
#     cost = float(input("Nhập giá thay đổi: "))
#     for i in range (len(sanpham)):
#         if sanpham["ten"][i] == name:
#             sanpham["gia"][i] = cost
#             print("Đổi giá thành công: ", sanpham["ten"][i], sanpham["gia"][i])
#             return
#     print("Không tìm thấy sản phẩm")

# change_cost(sanpham)

# YC3
def insert_category (sanpham):
    for i in range (len(sanpham)):
        category = input("Nhập category:")
        sanpham["category"][i] = category
    print(sanpham)
insert_category(sanpham)