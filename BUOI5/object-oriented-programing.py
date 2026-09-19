class Employee: # Tên class: Employee
    def __init__(
        self, # self đại diện cho đối tượng đang được tạo 
        name,
        department,
        salary
    ):
        self.name = name 
        # self.name là nơi lưu dữ liệu của đối tượng
        # name: dữ liệu được truyền vào
        self.department = department
        self.salary = salary

# Tạo nhân viên Đạt
staff_Dat = Employee("Dat", "IT", 100)
staff_Quan = Employee ("Quan", "IT", 200)
staff_Trung = Employee ("Trung", "HR",300)
# Truy cập vào thuộc tính
# employee["name"] -> dùng cho dictionary 
List_staff = {staff_Dat, staff_Quan, staff_Trung}
# Form nhân sự:
# Tên: ............
# Phòng ban:.......
# Lương:...........

# Ví dụ: 
# Object: hồ sơ của một nhân viên 
# Class: mẫu hồ sơ nhân viên 

# Dictionary




class CEO:
    def __init__ (self, name, department, salary, list_nv):
        self.name = name
        self.department = department
        self.salary = salary
        self.list_nv = list_nv
    def print_employee (self):
        for nv in self.list_nv:
            print("Ten: ", nv.name)
            print("Phong ban: ", nv.department)
            print("Luong: ", nv.salary)
    def salary_by_department (self):
        result = {}
        for nv in self.list_nv:
            phongban = nv.department
            luong = nv.salary
            if phongban in result:
                result[phongban] += luong
            else:
                result[phongban] = luong
        return result
sep = CEO("SEP", "Manager", 2000, List_staff)
sep.print_employee()
result = sep.salary_by_department()
print(result)
    # Method in ra thông tin nhân viên 
    
    # Method tính tổng lương theo phòng ban
   

    


# result = ceo.salary_by_department()
# print(result)