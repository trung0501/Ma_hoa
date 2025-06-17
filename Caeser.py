# Ham thuc hien ma hoa Caesar
def ma_hoa_caesar(chuoi_van_ban, khoa):
    ket_qua = ""
    for ky_tu in chuoi_van_ban:
        # Kiem tra neu la chu cai in hoa
        if ky_tu.isalpha() and ky_tu.isupper():
            # Dich chuyen ky tu theo khoa, đam bao quay vong trong 26 chu cai
            ma_hoa = (ord(ky_tu) - ord('A') + khoa) % 26 + ord('A')
            ky_tu_moi = chr(ma_hoa)
            ket_qua += ky_tu_moi
        else:
            # Neu khong phai chu in hoa, giu nguyen ky tu
            ket_qua += ky_tu
    return ket_qua

# Du lieu đau vao
chuoi_goc = "NGUYENTIENTRUNG"
khoa = 5

# Goi ham đe thuc hien ma hoa
chuoi_da_ma_hoa = ma_hoa_caesar(chuoi_goc, khoa)

# In ket qua
print("Chuỗi sau khi mã hóa:", chuoi_da_ma_hoa)