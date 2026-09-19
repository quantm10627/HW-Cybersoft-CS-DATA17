number = input("Nhập danh sách số nguyên: ")
ds = number.split(",")
for i in range (len(ds)):
    ds[i] = int(ds[i])

ds_le = []
ds_chan = []
for i in range(len(ds)):
    if ds[i] % 2 == 0:
        ds_chan.append(ds[i])
    else:
        ds_le.append(ds[i])
print("Danh sách chẵn: ", ds_chan)
print("Danh sách lẽ: ", ds_le)