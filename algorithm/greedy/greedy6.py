# greedy  주유소 
# 1 입력 : 도시 수 , 
# 2 입력: 도시수-1 수의 도로 ,
# 3 입력: 각 도시 별 기름가격 

#최소 주유 가격으로 각 도시 탐방하기
#내림차순의 경우 (작은 수) 주유를 하면 된다. 

city_num=int(input())
path=list(map(int,input().split()))
charge=list(map(int,input().split()))

result=0
liter=charge[0] #리터 가격 저장소(가장 작은 리터 값 저장)

for i in range(len(path)):
    result+=path[i]*liter
    if liter>charge[i+1]:
        liter=charge[i+1]
print(result)