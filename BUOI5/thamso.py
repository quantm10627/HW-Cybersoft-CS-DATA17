

class Employee: # Tên class: Employee
    def __init__(
        self, # self đại diện cho đối tượng đang được tạo 
        name = None,
        department = None,
        salary = None
    ):
        self.name = name 
        # self.name là nơi lưu dữ liệu của đối tượng
        # name: dữ liệu được truyền vào
        self.department = department
        self.salary = salary

staff1 = Employee("Quan")
print(staff1.name, staff1.department, staff1.salary)