'''
- 인덱스의 노드들이 향하는 위치에 대한 list저장 (0)
- 빈 스택을만든다 -> why? 인덱스의 노드가 향하는 위치만 뽑아와서 가져오고 다시 돌아간다
- visited에 대한 정보를 담는다 이미 인덱스의 노드로 향했다면, 그 노드는 결과에 다다를수없으므로 다음 노드를 search
'''
import sys; sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # V: V개 노드, E: E개 간선
    forword_node = [[] for _ in range(V+1)]
    for i in range(E):
        start, goal = map(int, input().split())
        forword_node[start].append(goal)

    S, G = map(int, input().split())
    ### forword_node = [[], [4, 3], [3, 5], [], [6], [], []] 까지만듬 ###
    stack = [] # 스택만들기
    visited = [False]*(V+1) # visited 만들기
    visited[S] = True
    stack.append(S)
    connected = False

    while stack:
        v = stack.pop()
        if v == G:
            connected = True
            break

        for w in forword_node[v]:
            if not visited[w]:
                visited[w] = True
                stack.append(w)

    if connected:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')