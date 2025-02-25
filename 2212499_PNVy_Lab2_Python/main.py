import datetime
from bai1 import SinhVien,DanhSachSV

noidung=DanhSachSV()


def DocFile():
    f= open("file.txt","r")
    for line in f:
       field= line.split(",")    
       maso=int(field[0])
       hoten=field[1].strip()
       ngaysinh=datetime.datetime.strptime(field[2].strip(),"%d/%m/%Y")
       sv=SinhVien(maso,hoten,ngaysinh)
       noidung.themSinhVien(sv)
    f.close()


#DocFile()
#noidung.xuat()




# n=input("Nhập tên Sinh Viên :")

# def tim_sv_theo_ten(n):  
#     DocFile()
#     k= noidung.TimSVTheoTen(n)
#     if k==-1:
#      print("không có Sinh Viên trong danh sách")
#     else:
#        print(noidung.dssv[k])

# tim_sv_theo_ten(n)


def tim_sv_truoc_ngay(n):
    DocFile()
    k=noidung.timSVTruocNgay(n)
    if k==-1:
       print("không có Sinh Viên trong danh sách")
    else: 
        print(noidung.dssv[k])



a=(input("Nhập ngày sinh dưới định dạng:dd/mm/yyy:"))
n=datetime.datetime.strptime(a,"%d/%m/%Y")
tim_sv_truoc_ngay(n)
