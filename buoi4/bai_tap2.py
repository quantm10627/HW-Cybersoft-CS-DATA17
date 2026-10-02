danh_sach = ["An", "Anh", "Binh", "Bich", "Bao"]
def Function (danh_sach):
    result = []
    for ten in (danh_sach):
        if ten.startswith("B"):
            result.append(ten)
    return result

n = Function(danh_sach)
if (n == 0):
    print("Khong tim thay")
else:
    print(Function(danh_sach))