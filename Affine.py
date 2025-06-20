def ma_hoa_affine(ban_ro, a, b):
    result = ""
    for ky_tu in ban_ro:
        if ky_tu.isalpha():
            x = ord(ky_tu.upper()) - ord('A')
            cipher_val = (a * x + b) % 26
            result += chr(cipher_val + ord('A'))
        else:
            result += ky_tu
    return result

# Dữ liệu đầu vào
plaintext = "NGUYENTIENTRUNG"
a, b = 5, 1

# Gọi hàm để thực hiện mã hóa
ciphertext = ma_hoa_affine(plaintext, a, b)

# Kết quả
print("Bản rõ:    ", plaintext)
print("Khóa (a,b):", (a, b))
print("Mã hóa:    ", ciphertext)
