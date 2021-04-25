money=False
if money:
    print("택시 타")
else:
    print("걸어가")

treeHit = 0
while treeHit<2:
    treeHit=treeHit +1
    print("나무를 %d번 찍었습니다." %treeHit)
    if treeHit==100:
        print("나무 넘어갑니다.")

x=2000
if x >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라.")

card = True
if x >=3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

print(1 in [1,2,3])  #1이 있는가? 
print(1 not in [1,2,3]) #1이 없는가?
print('a' in ('a','b','c'))
print('j' not in 'python')

pocket = ['paper','callphone','money']
if 'money' in pocket:
    print("택시를 타고 가라.")
else:
    print("걸어가라.")


# 아무것도 하지 않는 경우 pass

if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라.")


# 다중조건

pocket=['paper','cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라.")
elif card:
    print("카드계산 택시를 타고가라.")
else:
    print("걸어가.")

# if 한 줄 작성하기
if 'money' in pocket: pass
else: print("카드를 꺼내라.")

coffee =10
money= 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee-1
    print("남은 커피 양은 %d개 입니다." %coffee)
    if coffee==0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break


#coffee=10
#while True:
#   money= int(input("돈을 넣어주세요 :")) #직접 입력 받는거?
#    if money==300:
#       print("커피를 줍니다.")
#        coffee= coffee-1
#    elif money>300:
#        print("거스름 돈 %d 를 주고 커피를 줍니다." %(money-300))
#        coffee=coffee-1
#    else:
#        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#        print("남은 커피의 양 %d 개 입니다." %coffee)
#    if coffee==0:
#        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#        break

    a=0
    while a<10:
        a=a+1
        if a%2 ==0:continue
        print(a)
  
   # while True:
   #     print("컨트롤 씨 눌러야 while문 빠져 나갈 수 있습니다.")

a= [(1,2),(3,4),(5,6)]
for (first,last) in a:
    print(first+last)

marks=[90,25,67,45,80]
number =0
for mark in marks:
    number=number+1
    if mark >=60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)

number=0
for mark in marks:
    number=number+1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." %number)


add=0
for i in range(1,11):
    add=add+i

    print(add)

marks=[90,25,67,45,80]
for number in range(len(marks)):
    if marks[number] <60:
        continue
    print("%d번 학생 축하합니다. 합격입니다."%(number+1))

for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ") #이거 왜 줄 넘어가냐
        print(' ')


a=[1,2,3,4]
result=[]
for num in a:
    result.append(num*3)
    print(result)

a=[1,2,3,4]
result=[num*3 for num in a]
print(result)

result = [num*3 for num in a if num%2==0]
print(result)