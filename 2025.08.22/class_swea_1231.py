### 중위 순회 software ###
# import sys; sys.stdin = open("input.txt")

for tc in range(1, 11):
    N = int(input())
    l_child = [0]*(N+1)
    r_child = [0]*(N+1)
    word = [0]*(N+1) # 단어를 집어넣자 !

    for _ in range(N):
        lst = list(input().split()) # 정점, 단어, l자식, r자식 순
        if len(lst) != 4:
            if len(lst) == 3:
                lst.append(0)
            if len(lst) == 2:
                lst.append(0)
                lst.append(0)
        word[int(lst[0])] = lst[1]
        l_child[int(lst[0])] = int(lst[2])
        r_child[int(lst[0])] = int(lst[3])

    # print(l_child)
    # print(r_child)
    # print(word)
    sentence = []
    def f(root):
        if l_child[root] != 0:
            f(l_child[root])

        sentence.append(word[root])

        if r_child[root] != 0:
            f(r_child[root])

    f(1)
    print(f'#{tc}', ''.join(sentence))