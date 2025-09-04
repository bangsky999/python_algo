### 전자 카트 ###

T = int(input())


def f(idx, sum, prev_num):
    global min_val, e, visited, out

    # idx: 내가 만들어지는 순열의 몇번째의 숫자를 뽑고 있는지
    # sum: 현재까지 누적된 합, 순열에서 숫자를 뽑을 때마다 합을 누적해나간다.
    # prev_num: 이전 숫자

    # 기저조건
    if idx == N-1:
        sum += e[prev_num][1]
        if sum < min_val:
            min_val = sum
        return

    # 가지치기
    if sum >= min_val: # 현재 누적합이 직전에 구한 최소값보다 크거나 같다면
        return  # 그 이후는 볼 필요도 없으므로 그냥 리턴


    # 유도조건
    # 2부터 N까지의 숫자 중에서 하나를 뽑을 수 있지만
    # 이전에 아직 뽑지않은 숫자 중에서만...

    for num in range(2, N+1):
        if not visited[num]:
            visited[num] = True
            out[idx] = num # num 숫자 뽑기
            f(idx+1, sum + e[prev_num][num], num)
            visited[num] = False



for tc in range(1, T+1):
    N = int(input())

    # 0번 ~ N-1번까지를 쓰고
    # 0번 : 사무실
    # 1번 ~ N-1번 : 구역
    # e = [list(map(int, input().split())) for _ in range(N)]


    # 1번 ~ N번까지를 그대로 쓰려면
    # 1번 : 사무실
    # 2번 ~ N번 : 구역
    e = [[0] * (N+1)]
    e2 = [[0] + list(map(int, input().split())) for _ in range(N)]
    e.extend(e2)

    # 순열
    # 2번 ~ N번 까지의 수(N-1개)의 모든 순열을 다 생성해야 함
    visited = [False] * (N+1) # N번까지의 숫자를 쓰기 위해 N+1 길이로 만들기

    out = [0] * (N-1) # (N-1개)의 순열을 생성


    min_val = float('inf')

    f(0, 0, 1) 
    # 순열에서 0번째 숫자 뽑고, 현재합은 0, 사무실에서 출발했음.

    print(f"#{tc} {min_val}")


