def binary_search(arr, start, end, target):
    
    # print(f"start = {start}, end = {end}, mid = {mid}")
    if start >= end:
        return 0

    mid = (start+end)//2

    if target == arr[mid]:
        return 1
    
    
    if target < arr[mid]:
        return binary_search(arr,start,mid,target)
    else:
        return binary_search(arr, mid+1, end, target)

# N = int(input())
# num_arr = list(map(int,input().split(" ")))
# M = int(input())
# target_arr = list(map(int,input().split(" ")))

N = 5
num_arr = [4,1,5,2,3]
M = 5
target_arr = [1,3,7,9,5]
num_arr.sort()

for x in target_arr:
    print(binary_search(num_arr, 0, N, x))