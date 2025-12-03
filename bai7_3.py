print("Sinh vien: Nguyen Gia Huy")
print("Ma so SV : 245752021610165")
print("##########################")
# Duong dan toi tep van ban
ten_tep = "vanban.txt"

try:
    # Mo tep o che do doc ('r')
    with open(ten_tep, 'r', encoding='utf-8') as file:
        # Doc toan bo noi dung
        noi_dung = file.read()
    
    # In ra noi dung cua tep
    print(noi_dung)
except FileNotFoundError:
    print(f"Khong tim thay tep: {ten_tep}")
except Exception as e:
    print(f"Da xay ra loi: {e}")    
