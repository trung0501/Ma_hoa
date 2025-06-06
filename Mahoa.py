def ma_hoa(s):
    for i in range(len(s)):
        if s[i] == 't':
            s = s[:i] + 'r' + s[i+1:]
        elif s[i] == 'r':
            s = s[:i] + 'u' + s[i+1:]
        elif s[i] == 'u':
            s = s[:i] + 'n' + s[i+1:]
        elif s[i] == 'n':
            s = s[:i] + 'g' + s[i+1:]
        elif s[i] == 'g':
            s = s[:i] + 't' + s[i+1:]
    return s
k = input ('Nhap chuoi can ma hoa:')
print ('Chuoi ma hoa:', ma_hoa(k.lower()))