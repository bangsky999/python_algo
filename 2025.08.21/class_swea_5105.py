from collections import deque


# 상하좌우 탐색을 위한 델타배열
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 미로의 거리

T = int(input()) # 테스트케이스 수

for tc in range(1, T+1):
    N = int(input()) # 2차원 배열의 크기
    # 숫자가 공백 없이 들어오는 경우
    # input()으로 들어오는 문자열을 하나씩 순회하면서 정수로 바꿔줌
    # [int(n) for n in "13101"]
    # [1, 3, 1, 0, 1]

    arr = [[int(n) for n in input()] for _ in range(N)]
    # 방문처리 배열
    visited = [[False]*N for _ in range(N)]

    # 시작점, 도착점 좌표를 저장할 변수
    start_r, start_c, end_r, end_c = -1, -1, -1, -1
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                start_r, start_c = r, c
            elif arr[r][c] == 3:
                end_r, end_c = r, c

    # 2차원 배열 자체가 그래프로 해석할 수 있음
    # => 따로 인접행렬이나 인접리스트로 나타낼 필요가 없음.
    # 바로 BFS 알고리즘 적용

    # BFS 알고리즘
    # 1. 큐를 만든다.
    q = deque()

    # 2. 시작점을 방문처리 후, 큐에 넣는다.
    visited[start_r][start_c] = True # 시작점 방문처리
    q.append((start_r, start_c, 0))
    # 노드의 표현: 튜플 (r좌표, c좌표, 레벨(깊이))

    
    can_reach = False # 목적지에 도달할 수 있는지 여부 검사용 변수 #### 왜 필요한가
    maze_length = 0 # 목적지에 도달했다면, 그때의 길이를 저장할 변수 ### 왜 필요한가


    # 3. 큐에 원소가 있다면 계속 반복(큐가 빌 때까지)
    while q: # 큐에 원소가 있다면
        r, c, level = q.popleft() # 큐에서 원소를 꺼낸다.
        # (r, c) : 현재 탐색중인 노드 v

        # 노드 v를 기준으로 해서 모든 인접한 노드 중에서
        # 아직 방문하지 않은 노드를 찾아서 큐에 넣는다.
        # 인접 노드의 탐색: 상하좌우 델타 탐색
        # 상하좌우를 일단 보고, 만약에 노드가 있다면 => 인접 노드가 있는 것임
        # 그 중에서도 아직 방문하지 않은 노드를 방문처리 후 큐에 추가
        for d in range(4):
            nr, nc =  r + dr[d], c + dc[d]
            # 경계조건 체크
            if 0 <= nr < N and 0 <= nc < N:
                # 인접노드? (nr, nc)가 0이거나 3이면 인접노드, 1이면 노드가 아님
                if arr[nr][nc] == 0 and not visited[nr][nc]: # 인접노드이면서 아직 방문하지 않은 노드라면
                    visited[nr][nc] = True
                    q.append((nr, nc, level + 1))

                if arr[nr][nc] == 3: # 인접노드가 목적지
                    can_reach = True # 도착할 수 있음
                    maze_length = level # 목적지까지의 거리 저장
        
    print(f"#{tc} {maze_length}")


        