V = int(input()) # 정점의 개수, 정점번호는 1번부터 V번까지
arr = list(map(int, input().split()))

lft_child = [0] * (V+1) # 1 ~ V까지 인덱스가 필요하므로
rgt_child = [0] * (V+1)

for i in range(V-1):
    parent, child = arr[2*i], arr[2*i + 1]
    print(parent, child)
    if lft_child[parent] == 0:
        lft_child[parent] = child
    else:
        rgt_child[parent] = child

print(lft_child)
print(rgt_child)