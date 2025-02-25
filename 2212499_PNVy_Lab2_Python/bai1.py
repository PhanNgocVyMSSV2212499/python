import datetime


class SinhVien:
    truong="Đại học Đà Lạt"


    def __init__(self,maSo:int,hoTen:str,ngaySinh) -> None:
        self.__maSo=maSo
        self.__hoTen=hoTen
        self.__ngaySinh=ngaySinh

    
    @property
    def maSo(self):
        return self.__maSo
    
    @maSo.setter
    def maSo(self,maso):
        self.__maSo=maso
        
    @property
    def ngaySinh(self):
        return self.__ngaySinh

    @property
    def hoTen(self):
        return self.__hoTen
    
    @hoTen.setter
    def hoTen(self,hoTen):
        self.__hoTen=hoTen

    @staticmethod
    def laMaSOHopLe(maso:int):
        return len(str(maso))==7
    
    @classmethod
    def doiTenTruong(self,tenmoi):
        self.truong=tenmoi

    def __str__(self) -> str:
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"
    
    def Xuat(self):
        print (f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")

class DanhSachSV:
    def __init__(self) -> None:
        self.dssv=[]
    
    def themSinhVien(self,sv:SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    def timSvTheoMssv(self,mssv:int):
        return[sv for sv in self.dssv if sv.maSo==mssv]
    
    def XoaSVTheoMSSV(self,maSO:int):
        vt=self.timSvTheoMssv(maSO)
        if vt!=-1:
            del self.dssv[vt]
            return True
        else:
            return False
        
    def TimSVTheoTen(self,ten:str):
        for i in range(len(self.dssv)):
            if self.dssv[i].hoTen==ten:
                return i
        return -1
    

    def timSVTruocNgay(self,ngay:datetime):
        for i in range(len(self.dssv)):
             if self.dssv[i].ngaySinh>ngay:
                 return i
        return -1

