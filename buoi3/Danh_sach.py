ds = [1,2,3,4,5,6,7,8]
print(ds)

#Có 4 tính năng: Thêm, Xóa, Sửa, Tìm kiếm
#Thêm : tên_list.append(phần tử) , thêm phần tử vào cuối danh sách
ds.append(9)
print(ds)

#Insert: Thêm phần tử sau vị trí xác định
#Cú pháp: tên_list.insert(vị trí, phần tử)
ds.insert(0,0)
print(ds)

#Cập nhật phần tử
#Cú pháp: ds[index] = giá trị mới
ds[2] = 10
print(ds)

#Remove: Xóa phần tử, nếu có nhiều phần tử giống nhau thì chỉ xóa phần tử đầu tiên
#Cú pháp: ten_list.remove(giá trị cần xóa)
ds.remove(10)
print(ds)

#Xóa theo vị trí index (Pop): Xóa phần tử theo vị trí index, nếu không có index sẽ xóa cuối
ds.pop(1)
print(ds)