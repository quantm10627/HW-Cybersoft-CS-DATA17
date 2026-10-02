import re
def validate_email(email): #YC2
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if re.match(email_pattern, email):
        return True
    else:
        return False

def validate_phone (phone): #YC3
    if not phone.isdigit() or len(phone) != 10:
        return False
    else:
        return True

# Yêu cầu 2 và 3
#Hàm nhập thông tin sinh viên (bao gồm nhập mã sinh viên, họ tên, lớp, email, số điện thoại) 
#Bên cạnh đó xử lý trường hợp email và số điện thoại sai định dạng 
def Nhap_thongtin_sinhvien ():
    maSV = input("Nhập mã sinh viên: ")
    tenSV = input("Nhập họ và tên sinh viên: ")
    lopSV = input("Nhập lớp của sinh viên: ")
    while True: #YC2
        email = input("Nhập email của sinh viên: ")
        if validate_email(email) == False:
            print("Email không hợp lệ, vui lòng nhập lại! ")
        else: 
            break
    while True: #YC3
            phone = input("Nhập số điện thoại của sinh viên: ")
            if validate_phone(phone) == False:
                print("Số điện thoại không hợp lệ, vui lòng nhập lại! ")
            else: 
                break
    SV_data = [maSV, tenSV, lopSV, email, phone]
    return SV_data


#Yêu cầu 5 (Hàm tính tuổi của sinh viên)
def tinh_tuoi(ngay_sinh):
    # tinh đến ngày hiện tại là 19/09/2026
    nam = ngay_sinh.split("/")[2]
    tuoi = 2026 - int(nam)
    thang = int(ngay_sinh.split("/")[1])
    ngay = int(ngay_sinh.split("/")[0])
    
    if thang > 9: #Chưa đủ tháng 
            tuoi -= 1
    elif thang == 9 and ngay > 19: #Chưa đủ ngày
            tuoi -= 1
    return tuoi

