# 잃어버린 괄호 
# 최소값을 구하기 위해서 작은수-큰수 => - 기준으로 괄호를 묶는다.
# 첫 수는 양수 
# +는 다 더한 후 모두 빼준다. 

num=input().split('-') #['55','50+40','30+20']
box=[] # resultbox 

for i in num:
    count=0
    add=i.split('+')
    for j in add:
        count+=int(j)
    box.append(count)

result=box[0]
for i in range(1,len(box)):
    result-=box[i]

print(result)
