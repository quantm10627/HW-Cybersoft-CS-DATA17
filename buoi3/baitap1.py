# cú pháp random : number = random.ranint(a,b) : a <= number <= b



import random


while True:
    User = int(input("Nhập số từ 1 đến 3: "))
    Bot = random.randint (0,4 )
    if User > Bot:
        print("User thắng")
        break

