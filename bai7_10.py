print("Sinh vien: Nguyen Gia Huy")
print("Ma so SV : 245752021610165")
print("##########################")
# ten file
filename = "Vanban.txt"

# doc noi dung
with open(filename, 'r', encoding='utf-8') as file:
    text = file.read()

# tach thanh danh sach sach tu, bo cac ki tu xuong dong
words = text.replace("\n", " ").split()

# tim do dai tu dai nhat
max_length = max(len(word) for word in words)

# lay danh sach cac tu dai nhat
longest_words = [word for word in words if len(word) == max_length]

# loai trung lap
longest_words = list(set(longest_words))

print("Nhung tu dai nhat trong van ban:")
for word in longest_words:
    print(word, "(do dai:", len(word), ")")
