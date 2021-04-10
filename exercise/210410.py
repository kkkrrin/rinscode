#리스트 관련함수 

a=[1,2,3]
a.append(4)
print(a)

a.append([5,6])
print(a)

a=[1,4,3,2]
a.sort()
print(a)

a=['a','c','b']
a.reverse()
print(a)

a=[1,2,3]
a.index(3)
print(a.index(3))

a=[1,2,3]
a.insert(0,4)
print(a)

a.insert(3,5)
print(a)

a=[1,2,3,1,2,3]
a.remove(3) #첫 번째로 나오는 3을 삭제하는 함수, 중복시 첫 번째만 삭제된다.
print(a) 

a=[1,2,3]
print(a.pop()) #마지막 요소를 돌려주고 그 요소는 삭제한다.
print(a)

a=[1,2,3]
print(a.pop(1))
print(a) #1번째 요소를 돌려주고 그 요소를 삭제한다.


