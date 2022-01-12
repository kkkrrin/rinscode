# ATM 
# 대기시간 + 각자 인출하는데 걸리는 시간

print('how many people?')
n=int(input())

#시간을 배열로 입력받는다. 
print('time?')
time=list(map(int, input().split()))

# 대기시간 최소화를 위해 오름차순으로 정렬한다.
time.sort()

prev=0 # 대기시간 누적
total_sum=0 # 대기시간 + 각각 인출하는데 걸리는 시간

for i in range(n):
    total_sum+=prev+time[i]
    prev+=time[i]

print(total_sum)