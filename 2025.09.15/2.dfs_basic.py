'''
주어진 문제는 모든 경로를 찾는게 아니라 '탐색'이 목적이기에 
방문처리 취소 필요가 없음.
'''
def dfs(node):
    # 다음 재귀 호출
    # node로 부터 갈 수 있는 노드들을 모두 확인
    # --> 그 중에서 한곳으로 진행
    for next_node in graph[node]:
        # 이미 방문한 지점은 가지마라 !
        if visited[next_node]:
            continue

        visited[next_node] = 1
        dfs(next_node)

V, E = map(int,input().split())

# 인접 리스트 ( 연결된 간선만 저장 )
graph = [[] for _ in range(V+1)]
for _ in range(E):
    start, end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [0] * (V+1)
visited[1] = 1
dfs(1)