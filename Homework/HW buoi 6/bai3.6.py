def xoa_truong(data, field):
    # TODO
    
    if data.get(field) != None:
        value = data[field] # tao bien tam
        del data[field]
        return value
    else:
        return "Trường thông tin không tồn tại"
    pass

employee = {
    "name": "An",
    "department": "IT",
    "salary": 2000
}

print(xoa_truong(employee, "department"))
print(xoa_truong(employee, "phone"))
