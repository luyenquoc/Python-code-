d_t=float(input("Nhap diem toan:"))
d_l=float(input("Nhap diem ly:"))
d_h=float(input("Nhap diem hoa:"))
tong_diem=d_t+d_l+d_h
loai=""
if (tong_diem>=0) and (tong_diem<=2):   
    loai="kem"
elif (tong_diem>=3) and (tong_diem<5):
    loai="yeu"
elif (tong_diem>=5) and (tong_diem<=6):
    loai="trung binh"
elif (tong_diem>=7) and (tong_diem<8):
    loai="kha"
elif (tong_diem>8):
    loai="gioi"
print("Tong diem 3 mon thi:",tong_diem)
print("Thi sinh nay Xep loai:",loai)