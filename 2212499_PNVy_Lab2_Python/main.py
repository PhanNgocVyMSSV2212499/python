from fractions import Fraction 
class PhanSo:
    def __init__(self,TuSo:int,MauSo:int) -> None:
        self.__TuSO=TuSo
        self.__MauSO=MauSo


    @property
    def TuSo(self):
        return self.__TuSO
    
    @TuSo.setter
    def TuSo(self,TuSo):
        self.__TuSO=TuSo
        
    @property
    def MauSo(self):
        return self.__MauSO
    
    @MauSo.setter
    def MauSO(self,MauSo):
        self.__MauSO=MauSo


    def rutGon(self):
        return Fraction(self.__TuSO,self.__MauSO)
    
    
    def __add__(self,other):
        if isinstance(other,PhanSo):
           a= PhanSo(self.__TuSO*other.__MauSO+self.__MauSO*other.__TuSO,(self.__MauSO*other.__MauSO)*2) 
        return a.rutGon()
    

    def __sub__(self,other):
         if isinstance(other,PhanSo):
           a=PhanSo(self.__TuSO*other.__MauSO-self.__MauSO*other.__TuSO,(self.__MauSO*other.__MauSO)*2) 
           return a.rutGon()
         

    def __mul__(self,other):
        if isinstance(other,PhanSo):
            a= PhanSo(self.__TuSO*other.__TuSO,self.__MauSO*other.__MauSO) 
            return a.rutGon()
       
        

    def __truediv__(self,other):
        if isinstance(other,PhanSo):
            a= PhanSo(self.__TuSO*other.__MauSO,self.__MauSO*other.__TuSO) 
            return a.rutGon()

    def __repr__(self):
        return f"{self.__TuSO}/{self.__MauSO}"
    
a=PhanSo(2,3)
b=PhanSo(3,5)
c=PhanSo(-5,9)
d=PhanSo(20,6)
e=PhanSo(2,1)
print(f"{a}+{b}={a+b}")   
print(f"{a}-{b}={a-b}")
print(f"{a}*{b}={a*b}")
print(f"{a}/{b}={a/b}")
ps:PhanSo
class DSPhanSO:
    def __init__(self) -> None:
        self.dsps=[]
    def themPhanSO(self,ps:PhanSo):
        self.dsps.append(ps)
    def Xuat(self):
        for ps in self.dsps:
            print(ps)
    def DemPhanSOAM(self):
        count=0
        for ps in self.dsps:
            if(ps.MauSO<0 or ps.TuSo<0):
                count=count+1
        return count

ds=DSPhanSO()
ds.themPhanSO(a)
ds.themPhanSO(b)
ds.themPhanSO(c)
ds.themPhanSO(d)
ds.themPhanSO(e)
ds.Xuat()
kq = ds.DemPhanSOAM()
print(kq)
   

