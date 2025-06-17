def ma_hoa_don_bang(chuoi_van_ban, khoa):
    ket_qua = []
    for ky_tu in chuoi_van_ban:
        if ky_tu.isupper():
            vi_tri = ord(ky_tu) - ord('A')
            ma_hoa = (vi_tri + khoa) % 26
            ket_qua.append(chr(ma_hoa + ord('A')))
        else:
            ket_qua.append(ky_tu)  # Giữ nguyên ký tự không phải chữ hoa
    return ''.join(ket_qua)

# Dữ liệu đầu vào
chuoi_goc = "NGUYENTIENTRUNG"
khoa = 5

# Gọi hàm để thực hiện mã hóa
chuoi_da_ma_hoa = ma_hoa_don_bang(chuoi_goc, khoa)

# In kết quả
print("Chuỗi sau khi mã hóa:", chuoi_da_ma_hoa)