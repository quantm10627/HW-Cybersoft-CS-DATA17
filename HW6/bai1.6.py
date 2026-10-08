# Khai bao dictionary product
product = {
    "id" : ["0001", "0002", "0003"],
    "name" : ["Thit heo", "Rau cai", "Trai xoai"],
    "price" : ["100", "200", "300"],
    "quantity" : [1,2,3]
}

# YC1: In ten
print(product["name"])

#YC2 : Đổi giá. VD đổi giá thit thanh 1
product ["price"][0] = 1


#YC3: Them category
product["category"] = ["Thit", "Rau", "Trai cay"]


#YC4: Xoa quantity
del product["quantity"]
print("In danh sach product",product)
