T = int(input())

# 재귀호출 : Stack을 사용하는 것임
#  - DFS와 유사




def f(idx, sum):
    global min_sum

    # idx: 현재 선택해야 하는 행의 index
    # sum: 직전까지 선택한 모든 수의 합
    # 1. 기저조건
    if idx == N: # 행은 0, ... , N-1까지만 있음, N은 범위를 벗어남
        # 깊이 우선 탐색에서 마지막 깊이까지 왔음
        if sum < min_sum: # 누적합이 더 작은 것을 발견했다면 최소값 업데이트
            min_sum = sum # 할당문이 있다면 로컬 변수로 인식
            # print(min_sum) # 읽기만 하는 경우: global 키워드를 사용하지 않아도 됨
        return # 종료
    
   

    # 1.1. 가지치기
    if sum >= min_sum: # 직전 깊이 우선 탐색에서 찾은 최소값보다 현재 누적합이 크거나 같다면
        return # 조기 종료



    # 2. 유도조건
    # 2.1. 열 번호를 차례로 순회 (i: 0, ... , N-1)
    # 2.2. 열 번호 중에서 아직 선택하지 않은 열번호 하나를 선택
    #  (세로상에 겹치지 않는 수만 선택할 수 있음 => visited 배열로 관리)
    #  (이전에 선택하지 않은 열 idx만 선태갈 수 있음)
    # 2.3. 그 다음 행 선택하러 가기 f(idx+1, sum+선택한 수) 호출

    # idx: 행의 인덱스, i: 열의 인덱스

    for i in range(N):
        if not visited[i]: # 이전에 i번째 열을 선택하지 않았다면
            visited[i] = True # 선택을 하고
            f(idx+1, sum + arr[idx][i]) # 그 다음번 행 뽑으러 가기
            visited[i] = False # 선택 초기화(i는 독립적)



for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 재귀함수 설계하기
    # 한번에 모든 행의 숫자를 선택 x
    # 한번에 한 행만 선택한 후, 나머지는 그 다음 함수 호출에 넘기기

    # 합을 구하는 문제
    # 행에서 특정 숫자를 선택할 때마다 합이 누적됨.
    # 재귀 호출을 하면서 합을 누적해 나가는 것이 효율적

    visited = [False] * N # 처음에는 모든 열을 선택하지 않은 상태로 출발
    min_sum = float('inf') # 최소값은 최대값으로 초기화 
    # min_sum은 글로벌 변수로 선언

    f(0, 0) # 0번 행에서 숫자 선택하기, 처음에는 합이 0으로 출발.


    print(f"#{tc} {min_sum}")