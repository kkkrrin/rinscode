 # 연습문제 2장
 #6번

b = [1,3,5,4,2]
print(b)
b.reverse()
print(b)

#7번
a=['life','is','too','short']
print(" ".join(['life','is','too','short']))
#8번

t1= (1,2,3)
t2= (6,4) #그냥 4만 넣으면 안돼 왜?
c=t1+t2
print(c)

#9번 몰라
a=dict()
print(a)

#10번

a={'A':90,'B':80,'C':70}
print(a['B'])

#11번
a= set([1,1,1,2,2,3,3,3,4,4,5])
print(a)

#12번

a=b=[1,2,3]
a[1]=4
print(b)
# 같다고 선언해서.a가 변경되면 b도 같이 변경된다. 