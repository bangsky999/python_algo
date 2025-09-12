# {1,2,3,4,5,6,7,8,9,10}의 powerset 중 원소의 합이 10인 부분집합을 모두 출력하시오.
arr = [1,2,3,4,5,6,7,8,9,10]
# visited = [] -> 이번 문제는 사용할 필요 X

# level : N개의 원소를 모두 고려하면
# branch : 집합에 해당 원소를 포함시키는 경우 or 포함 X 경우
# 누적 값
#   - 부분집합의 총합
#   - 부분집합에 포함된 원소들

def dfs(cnt, total, subset):
    # 1. total이 10이면 출력해라
    if total == 10:
        print(subset)
        return
    
    # 2. total이 10을 넘으면 가지치기 하자
    if total > 10:
        return
    
    if cnt == 10:
        # 1. total이 10이면 출력해라 -> 여기서는 해도 안된다. (어차피 앞에서 걸림)
        return
    
    dfs(cnt+1, total + arr[cnt],subset+[arr[cnt]])
    dfs(cnt+1,total, subset)

dfs(0,0, [])