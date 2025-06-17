# Hàm thực hiện mã hóa Caesar
def ma_hoa_caesar(chuoi_van_ban, khoa):
    ket_qua = ""
    for ky_tu in chuoi_van_ban:
        # Kiểm tra nếu là chữ cái in hoa
        if ky_tu.isalpha() and ky_tu.isupper():
            # Dịch chuyển ký tự theo khóa, đảm bảo quay vòng trong 26 chữ cái
            ma_hoa = (ord(ky_tu) - ord('A') + khoa) % 26 + ord('A')
            ky_tu_moi = chr(ma_hoa)
            ket_qua += ky_tu_moi
        else:
            # Nếu không phải chữ in hoa, giữ nguyên ký tự
            ket_qua += ky_tu
    return ket_qua

# Dữ liệu đầu vào
chuoi_goc = "NGUYENTIENTRUNG"
khoa = 5

# Gọi hàm để thực hiện mã hóa
chuoi_da_ma_hoa = ma_hoa_caesar(chuoi_goc, khoa)

# In kết quả
print("Chuỗi sau khi mã hóa:", chuoi_da_ma_hoa)