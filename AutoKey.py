def ma_hoa_autokey(ban_ro, khoa):
    ban_ro = ban_ro.upper()
    khoa = khoa.upper()
    
    # Khóa mở rộng: key + phần đầu của plaintext
    while len(khoa) < len(ban_ro):
        khoa += ban_ro[:len(ban_ro) - len(khoa)]

    cipher = []
    for p, k in zip(ban_ro, khoa):
        p_val = ord(p) - ord('A')
        k_val = ord(k) - ord('A')
        c_val = (p_val + k_val) % 26
        cipher.append(chr(c_val + ord('A')))
    
    return ''.join(cipher)

# Dữ liệu đầu vào
ban_ro = "NGUYENTIENTRUNG"
khoa = "CHUYENGIA"

# Gọi hàm để thực hiện mã hóa
ciphertext = ma_hoa_autokey(ban_ro, khoa)

# Kết quả
print("Văn bản gốc:     ", ban_ro)
print("Khóa:            ", khoa)
print("Mã hóa AutoKey:  ", ciphertext)