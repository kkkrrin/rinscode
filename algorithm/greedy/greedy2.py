#  큰 수의 법칙 
# 가장 큰 수를 K 번 더하고 두번째로 큰 수를 한 번 더하는 연산

# n,m,k 를 공백으로 구분하여 입력받기
n,m,k= map(int, input().split())

#n 개의 수를 공백으로 구분하여 입력받기
data= list(map(int, input().split()))

data.sort()
first=data[n-1]
second=data[n-2]

#가장 큰 수가 더해지는 횟수 (공식)
count= int(m/(k+1))*k
count += m%(k+1)

result=0
result += (count) * first
result += (m-count) * second

print(result)