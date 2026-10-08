employees = {
    "name": ["An", "Bình", "Chi", "Dũng"],
    "department": ["IT", "IT", "HR", "Finance"],
    "salary": [2000, 3000, 1500, 2500]
}
print("Duyệt dữ liệu employees và in mỗi nhân viên theo định dạng: Tên - Phòng ban - Lương. Dùng cùng một index cho ba list song song.")
for i in range (len(employees["name"])):
    print (employees["name"][i], "-",employees["department"][i], "-",employees["salary"][i] )