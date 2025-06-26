def tao_ma_tran_khoa(khoa):
    # Create a 3*3 matrix from the lock string (tạo ma trận 3*3 từ chuỗi khóa)
    return [[ord(khoa[i * 3 + j]) - 65 for j in range(3)] for i in range(3)]

def chia_khoi_ban_ro(ban_ro):
    # Divide the copy into 3 characters, add 'x' if missing (chia bản sao thành 3 ký tự, thêm 'x' nếu thiếu)
    while len(ban_ro) % 3 != 0:
        ban_ro += 'X'
    khoi = [ban_ro[i:i+3] for i in range(0, len(ban_ro), 3)]
    return khoi

def khoi_sang_vector(khoi):
    # Convert block 3 characters into 3x1 column vector (chuyển khối 3 ký tự thành vector cột 3*1)
    return [[ord(c) - 65] for c in khoi]

def ma_hoa_khoi(vector, ma_tran_khoa):
    # Multiply key matrix by vector (nhân ma trận khóa với vector)
    vector_ma_hoa = [[0] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            vector_ma_hoa[i][0] += ma_tran_khoa[i][j] * vector[j][0]
        vector_ma_hoa[i][0] %= 26
    return vector_ma_hoa

def ma_hoa_hill(ban_ro, khoa):
    # Hàm chính để mã hóa theo Hill Cipher
    khoa = khoa.upper()
    ban_ro = ban_ro.upper()

    if len(khoa) != 9:
        raise ValueError("Khóa phải có đúng 9 ký tự.")
    
    ma_tran_khoa = tao_ma_tran_khoa(khoa)
    cac_khoi_ban_ro = chia_khoi_ban_ro(ban_ro)

    ban_ma = ''
    for khoi in cac_khoi_ban_ro:
        vector = khoi_sang_vector(khoi)
        vector_ma_hoa = ma_hoa_khoi(vector, ma_tran_khoa)
        ban_ma += ''.join(chr(giatri[0] + 65) for giatri in vector_ma_hoa)

    return ban_ma

# Dữ liệu đầu vào
ban_ro = "NGUYENTIENTRUNG"
khoa = "TOTNGHIEP"

# Gọi hàm để thực hiện mã hóa
ban_ma = ma_hoa_hill(ban_ro, khoa)

# Kết quả 
print("Bản mã:", ban_ma)