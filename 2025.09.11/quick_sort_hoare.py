arr = [3,2,4,6,9,1,8,7,5]

# 피벗: 제일 왼쪽 요소
# 이미 정렬된 배열이나 역순으로 정렬된 배열에서 최악의 성능을 보일 수 있음

def hoare_partition1(left, right):
    pivot = arr[left]
    i = left + 1
    j = right

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1

        if i < j: # swap
            arr[i], arr[j] = arr[j], arr[i]

    # pivot과 j 위치를 swap
    arr[left], arr[j] = arr[j], arr[left]
    return j

def quick_sort(left, right):
    if left < right:
        pivot = hoare_partition1(left, right)
        quick_sort(left, pivot-1)
        quick_sort(pivot+1, right)

quick_sort(0,len(arr)-1)
print(arr)