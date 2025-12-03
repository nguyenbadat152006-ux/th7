print("Sinh vien: Nguyen Gia Huy")
print("Ma so SV : 245752021610165")
print("##########################")
# Danh sach can ghi vao file
my_list = ["bai1", "bai2", "bai3"]

# Mo file de ghi (w = ghi moi, neu file ton tai se bi ghi de)
with open("Vanban.txt", "w", encoding="utf-8") as file:
    for item in my_list:
        file.write(item + "\n")  # moi phan tu tren mot dong

print("Da ghi danh sach vao file 'Vanban.txt'")
