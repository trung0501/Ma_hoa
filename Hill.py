def tao_ma_tran_khoa(khoa):
    return [[ord(khoa[i * 3 + j]) - 65 for j in range(3)] for i in range(3)]

def chia_khoi_ban_ro(ban_ro):
    while len(ban_ro) % 3 != 0:
        ban_ro += 'X'
    khoi = [ban_ro[i:i+3] for i in range(0, len(ban_ro), 3)]
    return khoi

def khoi_sang_vector(khoi):
    return [[ord(c) - 65] for c in khoi]

def ma_hoa_khoi(vector, ma_tran_khoa):
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