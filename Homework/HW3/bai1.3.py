so = input("Nhập dãy các số nguyên: ")
ds = so.split(",")
for i in range (len(ds)):
    ds[i] = int(ds[i])
n = len(ds)

if n < 2:
    print("Không có phần tử lớn thứ 2 vì mảng có ít hơn 2 phần tử")
elif n == 2 and ds[0] == ds[1]:
    print("Mảng có duy nhất 2 phần tử và 2 phần tử bằng nhau nên không có phần tử lớn thứ 2")
else:
    max1 = ds[0]
    max2 = float ('-inf')

    for i in range(1,len(ds)):
        if max1 < ds[i]: #Tìm thấy số lớn nhất hiện tại
            max2 = max1
            max1 = ds[i]
        elif max2 < ds[i] and max1 != ds[i]:
            max2 = ds[i]

    if max1 == max2 or max2 == float('-inf'): #Tất cả các số trong mảng bằng nhau
        print("Tất cả các số trong mảng bằng nhau nên không có số lớn thứ 2")
    else:
        print("Số lớn thứ 2:", max2)