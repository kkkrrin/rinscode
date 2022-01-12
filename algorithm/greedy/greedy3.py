# n,k n개의 동전으로 k값을 만드는 최소값

n,k=map(int,input().split())
coin_types=[0]*n # 입력받은 코인 개수를 초기화한다.

for i in range(n):
    coin_types[i]=int(input()) # 코인 값 입력받기 

count =0 # 필요한 동전 개수

for i in range(n-1,-1,-1): #동전 크기 큰 것 부터 센다. 
    if coin_types[i]<=k: #코인값이 입력한 금액보다 작거나 같으면 실행
        temp=k//coin_types[i] # 몫 
        count+=temp # 몫 누적
        k-=temp*coin_types[i] # 나머지

print(count)

