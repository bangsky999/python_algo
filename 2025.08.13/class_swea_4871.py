T = int(input())


for tc in range(1, T+1):
    V, E = list(map(int, input().split()))

    # 그래프를 어떻게 저장할 것인가?
    # 인접행렬 또는 인접리스트로 저장

    # 인접 리스트인 경우
    # 노드 번호가 1번부터 ~ V번까지
    # 각 노드에 연결되어 있는 노드의 번호를 리스트 저장
    # => 2차원 리스트

    adj = [[] for _ in range(V+1)]
    # adj[1] : 1번과 연결되어 있는 노드 번호들
    # adj[V] : V번 노드와 연결되어 있는 노드 번호들

    for _ in range(E): # E개의 간선 정보를 입력받는다
        start, end = list(map(int, input().split()))
        adj[start].append(end) # start->end 간선을 인접리스트에 저장

    S, G = list(map(int, input().split()))
    # S: 출발점
    # G: 도착점

    # S와 G가 서로 연결되었는지?
    # S를 출발점으로해서 그래프 탐색
    # 그래프 탐색: 그래프의 모든 노드를 한번씩 방문
    # 그래프 탐색을 하는 도중에 G가 발견이 됨 : S, G는 연결됨
    # 그래프 탐색이 끝났음에도 G가 발견안됨: S에서 출발해서 G로 갈 수 없음

    stack = [] # DFS 탐색을 위해, 인접 노드를 저장할 스택
    connected = False # 연결안됨으로 가정
    # 중간에 G가 나오면 True로 바꿔주기

    visited = [0] * (V+1) # 방문처리 배열
    # 0으로 초기화(아직 아무 노드도 방문하지 않음.)
    # visited[1] == 0: 1을 방문하지 않은 상황
    # visited[1] == 1: 1을 이미 방문
    # visited[V] == 1: V 노드를 방문했음.

    # print(adj)

    # 1. 시작 점을 방문처리후 스택에 넣는다.
    visited[S] = 1
    stack.append(S)

    # 2. while문을 반복
    while stack: # stack이 비어있지 않다면
        # 2.1. stack에서 top을 제거
        # print(stack)

        v = stack.pop() # 현재 스택의 가장 위에 있는 노드 부터 방문

        # print(v)

        if v == G: # 만약 도착점을 방문했다면
            # print("도착점 방문!")
            connected = True
            break

        #adj[v]: v점에서 갈수있는 노드들(인접 노드)
        for w in adj[v]: # 인접 노드를 모두 검사
            if visited[w] == 0: # 아직 w를 방문하지 않았다면
                visited[w] = 1 # 방문 처리 후에
                stack.append(w) # 스택에 넣는다.
    
    if connected:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")


