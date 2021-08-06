from collections import deque

N = int(input())

deq = deque([i for i in range(1, N+1)])

while(len(deq)>1):
    deq.popleft()

    if(len(deq)==1):
        break

    temp = deq.popleft()
    deq.append(temp)
    

print(list(deq)[0])
