customer = {
    "name": "Minh",
    "email": "minh@gmail.com"
}
print (customer["email"])
# Dung ham get, cu phap: ten_dic.get(key, return value)
if customer.get("phone", 0) == 0:
    print("Chưa có số điện thoại")
else:
    print (customer["phone"])