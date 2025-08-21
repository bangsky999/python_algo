T = int(input())
def winner(l, r):
    global cards

    if l == r:
        return l
    
    mid = (l+r)//2

    l_winner = winner(l, mid)
    r_winner = winner(mid+1, r)

    if cards[l_winner] == cards[r_winner]:
        return l_winner
    
    if cards[l_winner] == 1:
        if cards[r_winner] == 2:
            return r_winner
        elif cards[r_winner] == 3:
            return l_winner
    elif cards[l_winner] == 2:
        if cards[r_winner] == 1:
            return l_winner
        elif cards[r_winner] == 3:
            return r_winner
    elif cards[l_winner] == 3:
        if cards[r_winner] == 1:
            return r_winner
        elif cards[r_winner] == 2:
            return l_winner
        
for tc in range(1, T+1):
    N = int(input())
    cards = [0] + list(map(int, input().split()))
    num = winner(1, N)
    print(f'#{tc} {num}')