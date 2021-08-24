# N = int(input())
# meetings = []


# for _ in range(N):
#     start, end = map(int,input().split())
#     meetings.append((start,end))

N = 11
meetings = [(1,4),(3,5),(0,6),(5,7),(3,8),(5,9),(6,10),(8,11),(8,12),(2,13)]
meetings= sorted(meetings, key=lambda x:x[0])

case = []

for start, end in meetings:
    temp = case[:]
    for i, x in enumerate(case):
        if (x[0] <= start < x[1]) or (x[0] < end <= x[1]):
            if (end-start)<(x[1]-x[0]):
                temp.remove(x)
                temp.a

















meetings= sorted(meetings, key=lambda x:x[1], reverse=True)

dic_t = {}  # end : [start]

for start,end in meetings:
    if end in dic_t.keys():
        dic_t[end].append(start)
    else:
        dic_t[end] = [start]



meetings= sorted(meetings, key=lambda x:x[0])

case_len = []

# 가능한 경우 찾는 코드
for i, x in enumerate(meetings):
    temp = [x]
    for y in meetings[i:]:
        if y[0] >= temp[-1][1]:
            temp.append(y)

    case_len.append(len(temp))

print(max(case_len))