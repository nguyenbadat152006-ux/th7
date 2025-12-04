
def count_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return len(file.readlines())
#vidu
filename = "C:/Users/khanh/Downloads/New folder/Vanban.txt.txt"
print("so dong trong tep:", count_lines(filename))

