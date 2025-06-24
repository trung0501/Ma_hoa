def tao_ma_tran_khoa(khoa):
    return [[ord(khoa[i * 3 + j]) - 65 for j in range(3)] for i in range(3)]

def chia_khoi_ban_ro(ban_ro):
    while len(ban_ro) % 3 != 0:
        ban_ro += 'X'
    khoi = [ban_ro[i:i+3] for i in range(0, len(ban_ro), 3)]
    return khoi