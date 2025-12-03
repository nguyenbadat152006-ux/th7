print("Sinh vien: Nguyen Gia Huy")
print("Ma so SV : 245752021610165")
print("##########################")
# Ten file nguon va file dich
source_file = "Vanban.txt"
destination_file = "SaoChepVanban.txt"

# Mo file nguon de doc va file dich de ghi
with open(source_file, 'r', encoding='utf-8') as src:
    content = src.read()  # doc toan bo noi dung

with open(destination_file, 'w', encoding='utf-8') as dest:
    dest.write(content)  # ghi vao file dich

print(f"Da sao chep noi dung tu '{source_file}' sang '{destination_file}'")
