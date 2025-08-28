### 강사님 풀이
N = int(input())

min_cnt = 9999999999

def dfs(num, cnt):
    global min_cnt
    # 기저 조건
    if num == 0:
        if cnt < min_cnt:
            min_cnt = cnt
        return
    if num < 0:
        return

    if cnt >= min_cnt:
        return

    # 유도 조건
    else:
        dfs(num-5, cnt+1)
        dfs(num-3, cnt+1)
        
dfs(N, 0)
if min_cnt == 9999999999:
    print(-1)
else:
    print(min_cnt)