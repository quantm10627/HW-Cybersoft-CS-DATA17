menu = ["Cua", "tôm", "cá", "cơm"]
loai_mon = ["cơm chiên", "cơm chiên", "cơm chiên", "hải sản", "hải sản"]
i = 0
for i in range(len(loai_mon)):
    loai_mon.remove("hải sản")
print(loai_mon)
