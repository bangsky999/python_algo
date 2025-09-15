from collections import deque


def bfs(start_node):
    # q의 의미: 다음에 방문해야할 노드들 (후보군)
    q = deque([start_node])

    while q:
        now = q.popleft()

        for next_node in graph[now]:
            if visited[next_node]:
                continue

            visited[next_node] = 1
            q.append(next_node)

V, E = map(int,input().split())

# 인접 리스트 (연결된 간선만 저장)
graph = [[] for _ in range(V+1)]
for _ in range(E):
    start, end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [0] * (V+1)
visited[1] = 1
bfs(1)