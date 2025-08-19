### 블랙잭 ###
N, M = map(int, input().split())
card_lst = list(map(int, input().split()))
max_num = 0
for i in range(0, N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if card_lst[i]+card_lst[j]+card_lst[k] <=M and card_lst[i]+card_lst[j]+card_lst[k] > max_num:
                max_num = card_lst[i]+card_lst[j]+card_lst[k]

print(max_num)
