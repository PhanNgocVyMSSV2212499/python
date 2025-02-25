from datetime import datetime
class Sach:
    def __init__(self,ten_sach,ten_tac_gia,ngay_xb,so_trang,gia_bia):
         self.ten_sach = ten_sach
         self.ten_tac_gia=ten_tac_gia
         self.ngay_xb=datetime.strptime(ngay_xb,"%Y-%m-%d")
         self.so_trang=so_trang
         self.gia_bia=gia_bia
    def __str__(self):
         return(f"{self.ten_sach}\t\t{self.ten_tac_gia}\t\t\t{self.ngay_xb}\t\t,{self.so_trang}\t\t{self.gia_bia}\t\t{self.tinhgiaban()}")

class sachgiay(Sach):
     def __init__(self,ten_sach,ten_tac_gia,ngay_xb,so_trang,gia_ban,trong_luong):
            super().__init__(ten_sach,ten_tac_gia,ngay_xb,so_trang,gia_ban)
            self.trong_luong=trong_luong

     def tinhgiaban(self):
          phivanchuyen=self.trong_luong*100
          giaban=(0.95*self.gia_bia)+phivanchuyen
          return giaban



class sachdientu(Sach):
    def __init__(self, ten_sach, ten_tac_gia, ngay_xb, so_trang, gia_bia,dung_luong):
         super().__init__(ten_sach, ten_tac_gia, ngay_xb, so_trang, gia_bia,)
         self.dug_luog=dung_luong

    def tinhgiaban(self):
         if self.dug_luog>=10:
              phuthu=10000
         else:
              phuthu=0
         gia_ban=0.75*self.gia_bia+phuthu
         return gia_ban


class dsSach:
     def __init__(self):
         self.ds=[]
     def them_sach(self, sach): 
        self.ds.append(sach)
     def xuat_danh_sach(self):
         print("Tên sách\t\tTên tác giả\t\tNăm xuất bản\t\tGiá bìa\t\tGiá bán")
         for sach in self.ds:
            print(sach)

danh_sach = dsSach()
danh_sach.them_sach(sachgiay("Sách A", "Shakespeare", "2000-05-15", 150, 120000, 1.2))
danh_sach.them_sach(sachdientu("Sách B", "Shakespeare", "1999-07-20", 190, 80000, 12))
danh_sach.them_sach(sachgiay("Sách C", "Nguyen Du", "2000-01-10", 200, 150000, 1.5))
danh_sach.them_sach(sachdientu("Sách D", "Nam Cao Tha", "2010-09-12", 300, 200000, 8))
danh_sach.them_sach(sachgiay("Sách E", "Shakespeare", "2005-03-18", 110, 100000, 0.8))

print("Danh sách sách:")
danh_sach.xuat_danh_sach()