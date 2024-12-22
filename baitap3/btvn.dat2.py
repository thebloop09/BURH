# Nhập vào số giây cần chuyển đổi
s = int(input("Nhập số giây: "))

# Tính số giờ
hours = s // 3600
# Tính số phút sau khi đã trừ đi số giây cho giờ
minutes = (s % 3600) // 60
# Tính số giây còn lại
seconds = s % 60

# In kết quả ra màn hình
print("{s} giây = {hours} giờ {minutes} phút {seconds} giây")


