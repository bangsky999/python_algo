V, E = map(int, input().split())

# 인접 행렬(0,1로 연결 유무를 모두 저장)
# 7*7의 0배열 (1~7의 정점 번호를 활용)
graph = [[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    start, end = map(int,input().split())
    graph[start][end] = 1
    graph[end][start] = 1

for row in graph[1:]:
    print(row[1:])

# 인접 리스트( 연결된 간선만 저장)
graph = [[] for _ in range(V+1)]
for _ in range(E):
    start, end = map(int,input().split())
    graph[start].append[end]
    graph[end].append[start]

for row in graph[1:]:
    print(row)