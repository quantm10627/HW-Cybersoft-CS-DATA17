employees = {
    "name": ["An", "Bình", "Chi", "Dũng"],
    "department": ["IT", "IT", "HR", "Finance"],
    "salary": [2000, 3000, 1500, 2500]
}

salary_by_department = {}

# TODO: dùng for + if + dictionary

for i in range (len(employees["name"])):
    department = employees["department"][i]
    salary = employees["salary"][i]
    if department not in salary_by_department:
        salary_by_department[department] = salary
    else:
        salary_by_department[department] += salary

print(salary_by_department)
