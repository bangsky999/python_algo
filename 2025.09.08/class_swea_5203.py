### 5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임 ### 
import sys;sys.stdin = open("input.txt")
'''
card가 [1,1,2,2,3,3]의 경우 sort해도 run을 확인할 수 없음.
'''

T = int(input())

def is_run(player): # [1,1,2,2,3,3]
    counting = [0]*10 # 0~9까지 카운트
    for i in player:
        counting[i] = player.count(i)
    for j in range(8): # 0 1 2 3 4 5 6 7 8 9
        if counting[j]>0 and counting[j+1]>0 and counting[j+2]>0:
            return True


def is_triplet(player):
    for i in player:
        if player.count(i)>=3:
            return True
            

for tc in range(1,T+1):
    winner = 0
    cards = list(map(int,input().split())) # [9 9 5 6 5 6 1 1 4 2 2 1]
    player1 = []
    player2 = []
    for i in range(len(cards)//2): # 0 1 2 3 4 5 
        player1.append(cards[i*2])
        player2.append(cards[i*2+1])

        if len(player1) >= 3 or len(player2) >= 3:
            # sort할 필요가 없음, 예외케이스 [1,1,2,2,3,3]
            # player1.sort()
            # player2.sort()
            # run, triplet 있는지 확인
            if is_run(player1) or is_triplet(player1): # 되어서 true가 나오면
                winner = 1
                break
            elif is_run(player2) or is_triplet(player2):
                winner = 2
                break
    
    if winner == 1:
        print(f'#{tc} {winner}')
    elif winner == 2:
        print(f'#{tc} {winner}')
    elif winner == 0:
        # 무승부라면 
        print(f'#{tc} {winner}')
            

