
#ex1
list1=[100,200,300,400,500]
list1.reverse()
print(list1)

#ex2
lista=["M","na","i","Ke"]
listb=["y","me","s","lly"]
listc=[lista[0]+listb[0],lista[1]+listb[1],lista[2]+listb[2],lista[3]+listb[3]]
print(listc)

listd=[i+j for i,j in zip(lista,listb)]
print(listd)


#ex3
numbers=[1,2,3,4,5,6,7]
a=[]
for i in numbers:
    a.append(i*i)

print(a)

#ex4
listy=["Hello ","take "]
listz=["Dear ","Sir "]
listkq=[a+b for a in listy for b in listz]
print (listkq)


#ex5
listq=[10,20,30,40]
listw=[100,200,300,400]
for p,q in zip(listq,listw[::-1]):
   print(p,q)

#for i in listq:
    #for j in listw: 
      #print(f"{i} {j}")

#ex6
liste=["Mike","","Emma","Kelly",",Brad"]
liste.remove("")
print(liste)

res=list(filter(None,liste))
print(res)

#ex7
list1f= [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1f[2][2].append(7000)
print(list1f)



#ex8
listb1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]
listb1[2][1][2].extend(sub_list)
print(listb1)



#ex9
listc1 = [5, 10, 15, 20, 25, 50, 20]
index=listc1.index(20)
listc1[index]=200
print (listc1)


#ex10
listg=[5,20,15,25,50,20]
def remove_value(slist,val):
    return[i for i in slist if i!=val]

res=remove_value(listg,20)
print (res)
