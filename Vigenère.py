def tao_khoa(van_ban, khoa):
    khoa = list(khoa)
    if len(van_ban) == len(khoa):
        return khoa
    else:
        for i in range(len(van_ban) - len(khoa)):
            khoa.append(khoa[i % len(khoa)])
    return "".join(khoa)

def ma_hoa_vigenere(van_ban, khoa):
    ma_hoa_van_ban = []
    khoa = tao_khoa(van_ban, khoa)
    for i in range(len(van_ban)):
        char = van_ban[i]
        if char.isupper():
            ma_hoa_char = chr((ord(char) + ord(khoa[i]) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            ma_hoa_char = chr((ord(char) + ord(khoa[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            ma_hoa_char = char
        ma_hoa_van_ban.append(ma_hoa_char)
    return "".join(ma_hoa_van_ban)

# Dữ liệu đầu vào
ban_ro = "NGUYENTIENTRUNG"
khoa = "CHUYENGIA"

# Gọi hàm để thực hiện mã hóa
ma_hoa_van_ban = ma_hoa_vigenere(ban_ro, khoa)

# Kết quả 
print(f"Văn bản mã hóa: {ma_hoa_van_ban}")