from collections import deque

N, n = map(int,input().split())
nums = list(map(int,input().split()))

lst = [i for i in range(1,N+1)]
count = 0
r = 0

for x in nums:
    l = len(lst)
    print("회전 전 : ",lst)
    if lst.index(x) <= l//2:
        r = lst.index(x) * (-1)
    else:
        r = l - lst.index(x) 

    count += abs(r)

    lst = deque(lst)
    lst.rotate(r)
    lst.popleft()
    lst = list(lst)
    
    print("회전 후 : ",lst)
    print("r값 : ",r)
    print()

print(count)