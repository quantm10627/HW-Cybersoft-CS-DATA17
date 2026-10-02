danh_sach = ["An", "Binh", "Quan", "Trung", "Dong"]
# def tim_vi_tri (name):
#     for i in range(0,len(danh_sach), 1):
#         if danh_sach[i] == name:
#             return i
#     return -1

# name = input("Nhap ten nguoi can tim: ")
# result = tim_vi_tri(name)
# if result == -1 :
#     print("Khong tim thay")
# else:
#     print("Vi tri so", result + 1)

def tim_ten(danh_sach, ten_can_tim):
    if ten_can_tim not in danh_sach:
        return "Khong ton tai"
    for i,ten in enumerate (danh_sach):
        if ten == ten_can_tim:
            return i+1
ten_can_tim = input("Nhap ten can tim: ")
print(tim_ten(danh_sach, ten_can_tim))

    