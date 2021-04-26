#3장 연습문제

#Q1
print("shirt 셔츠만 출력되는거같음.") 

#Q2 
n=1
while True:
    n=n*3
    if n>=1000:
        break
print(n)

#Q3 답이 가로로 안나오고 세로로 나옴 ㅡㅡ 

for i in range(0,6):
    for j in range(i):
        print("*")

    print("\n")
        

#Q4

for i in range(1,101):
    print("%d" %i)

  
#Q5

sum=0
aclass=[70,60,55,75,95,90,80,80,85,100]
for i in aclass:
    sum=sum+i
print("A학급의 평균 점수는 %d 입니다."%(sum/10))


#Q6

number=[1,2,3,4,5]
result=[ n*2 for n in number if n%2==1 ]
print(result)