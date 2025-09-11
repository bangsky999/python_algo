T = int(input())
for tc in range(1, T+1):
    N = int(input())

    def merge(left, right):
        # 두 리스트를 병합한 결과 리스트
        result = [0]*(len(left)+len(right))
        l = r = 0

        # 두 리스트에서 비교할 대상이 남아있을 때까지 반복
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result[l+r] = left[l]
                l += 1

            else:
                result[l+r] = right[r]
                r += 1

        # 하나를 먼저 다 사용했을 때
        while l < len(left):
            result[l+r] = left[l]
            l += 1

        while r < len(right):
            result[l+r] = right[r]
            r += 1

        return result

    def merge_sort(li):
        if len(li) == 1:
            return li
        
        # 1. 절반씩 분할
        mid = len(li)//2
        left = li[:mid]
        right = li[mid:]

        left_list = merge_sort(left)
        right_list = merge_sort(right)
        # 분할 완료
        merged_list = merge(left_list, right_list)
        return merged_list

    arr = list(map(int,input().split()))
    sorted_arr = merge_sort(arr)
    print(f'#{tc}', end = ' ')
    print(*sorted_arr)