

#def sum_of_first_n(n):
#    return n * (n + 1) // 2

#n=int(input("nhap n:"))
#print(sum_of_first_n(n))

def giai_thua(n): 
     if n == 0 or n == 1:
        return 1
     else:
        return n*giai_thua(n-1) 

n=int(input("Nhap n:"))
giatri=giai_thua(n)
print(giatri)
