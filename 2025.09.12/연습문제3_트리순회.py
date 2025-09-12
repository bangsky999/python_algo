arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

# Todo: 일차원 리스트로 저장한다면 어떻게 할까?

# [참고] 그래프처럼 저장하는 방식
nodes = [[] for _ in range(14)]

for i in range(0,len(arr),2):
    parent_node = arr[i]
    child_node = arr[i+1]
    nodes[parent_node].append(child_node)

# 자식이 없는 걸 표현하기 위해 None을 삽입
for li in nodes:
    for _ in range(len(li),2):
        li.append(None)

def order(node):
    if node == None:
        return
    
    # nodes[node]: node에 연결된 번호들(자식 번호들)
    # nodes[node][0]: 첫번째 자식번호
    # nodes[node][1]: 두번째 자식번호
    order(nodes[node][0])
    order(nodes[node][1])
    print(node, end = ' ')

order(1)