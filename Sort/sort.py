def insertion_sort(num_list):
    for i in range(1,len(num_list)):
        for j in range(i,0,-1):
            if num_list[j] < num_list[j-1]:
                num_list[j-1],num_list[j] = num_list[j],num_list[j-1]
    return num_list


def selection_sort(num_list):
    for i in range(1,len(num_list)):
        min_x = min(num_list[i:])
        idx = num_list.index(min_x)
        if num_list[i-1] > num_list[idx] :
            num_list[i-1], num_list[idx] = num_list[idx], num_list[i-1]
    return num_list


def bubble_sort(num_list):
    for i in range(len(num_list)-1):
        for j in range(0,len(num_list)-i-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list


# 함수 실행
n = int(input())
num_list = []


for _ in range(n):
    num = int(input())
    num_list.append(num)


insertion_sorted_list = insertion_sort(num_list)
print(" ".join(map(str, insertion_sorted_list)))


selection_sorted_list = selection_sort(num_list)
print(" ".join(map(str, selection_sorted_list)))

bubble_sorted_list = bubble_sort(num_list)
print(" ".join(map(str, bubble_sorted_list)))