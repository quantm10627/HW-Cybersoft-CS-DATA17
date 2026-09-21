number = input("Nhập danh sách số nguyên: ")
ds = number.split(",")
for i in range (len(ds)):
    ds[i] = int(ds[i])

for i in range (0,len(ds) - 1,1):
    temp = i
    for j in range(i,len(ds),1):
        if ds[j] < ds[temp]:
            temp = j
    ds[i], ds[temp] = ds[temp], ds[i]
    
print("Kết quả dãy số sau khi sắp xếp: ", ds)