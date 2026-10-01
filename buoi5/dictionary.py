employee = {
    "name": ["An", "Ánh", "Bình", "Bảo", "Bích", "Chi"],
    "department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "salary": [2000, 1000, 2200, 200, 1200, 2000]
}

# for i in range (len(employee)):
#     print ("Tên: ", employee["name"][i])
#     print ("Department: ", employee["department"][i])
#     print ("Salary: ", employee["salary"][i])

salary_by_department = {}
for i in range(len(employee["name"])):
    department = employee["department"][i]
    salary = employee["salary"][i]
    if department in salary_by_department:
        salary_by_department[department] += salary
    else:
        salary_by_department[department] = salary

print (salary_by_department)
