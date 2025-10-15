'''
맨 앞부터 가서 1차례에는 맨뒤에 가장 큰수가 나온다
- 하나씩 계속 크기를 비교하면서 간다
'''
def bubble_sort(li, a):
    for i in range(a-1, 0, -1):
        for j in range(i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                
    return li
N = int(input())
arr = [0]*N
for i in range(N):
    arr[i] = int(input())
aa = bubble_sort(arr, N)
for i in aa:
    print(i)