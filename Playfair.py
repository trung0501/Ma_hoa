def tao_bang_khoa(khoa):
    khoa = khoa.lower().replace(" ", "").replace("j", "i")
    da_dung = set()
    bang_khoa = []

    for ky_tu in khoa + ''.join(chr(i) for i in range(97, 123)):
        if ky_tu == 'j':
            continue
        if ky_tu not in da_dung:
            da_dung.add(ky_tu)
            bang_khoa.append(ky_tu)
        if len(bang_khoa) == 25:
            break

    return [bang_khoa[i*5:(i+1)*5] for i in range(5)]

def tim_vi_tri(bang_khoa, a, b):
    vi_tri = []
    for ky_tu in (a, b):
        if ky_tu == 'j':
            ky_tu = 'i'
        for i in range(5):
            for j in range(5):
                if bang_khoa[i][j] == ky_tu:
                    vi_tri.extend([i, j])
    return vi_tri

def chuan_hoa_van_ban(van_ban):
    van_ban = van_ban.lower().replace(" ", "").replace("j", "i")
    return van_ban if len(van_ban) % 2 == 0 else van_ban + 'z'

def ma_hoa(van_ban, bang_khoa):
    danh_sach_ky_tu = list(van_ban)
    for i in range(0, len(danh_sach_ky_tu), 2):
        dong1, cot1, dong2, cot2 = tim_vi_tri(bang_khoa, danh_sach_ky_tu[i], danh_sach_ky_tu[i+1])
        if dong1 == dong2:
            danh_sach_ky_tu[i] = bang_khoa[dong1][(cot1 + 1) % 5]
            danh_sach_ky_tu[i+1] = bang_khoa[dong2][(cot2 + 1) % 5]
        elif cot1 == cot2:
            danh_sach_ky_tu[i] = bang_khoa[(dong1 + 1) % 5][cot1]
            danh_sach_ky_tu[i+1] = bang_khoa[(dong2 + 1) % 5][cot2]
        else:
            danh_sach_ky_tu[i] = bang_khoa[dong1][cot2]
            danh_sach_ky_tu[i+1] = bang_khoa[dong2][cot1]
    return ''.join(danh_sach_ky_tu)

def ma_hoa_playfair(van_ban_goc, khoa):
    bang_khoa = tao_bang_khoa(khoa)
    van_ban_sach = chuan_hoa_van_ban(van_ban_goc)
    return ma_hoa(van_ban_sach, bang_khoa)

# Dữ liệu đầu vào 
khoa = "Chuyengia"
van_ban = "nguyentientrung"

# Gọi hàm để thực hiện mã hóa 
ma_hoa_van_ban = ma_hoa_playfair(van_ban, khoa)

# Kết quả 
print("Khóa:", khoa)
print("Văn bản gốc:", van_ban)
print("Văn bản mã hóa:", ma_hoa_van_ban)