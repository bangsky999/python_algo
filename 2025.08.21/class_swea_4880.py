### [파이썬 S/W 문제해결 기본] 5일차 - 토너먼트 카드게임 ###

T = int(input())


def winner(l, r):
    global cards
    # l: 왼쪽 끝 학생 번호, r: 오른쪽 끝 학생의 번호
    # 구간 [l, r]까지의 학생들 중에서 승자의 번호를 반환하는 함수

    # 1. 기저조건
    # 길이가 1개일 때까지 쪼갤 수 있다.
    if l == r:
        # 카드가 1개일 때는 본인이 승자
        return l
    
    # 2. 유도조건
    # 현재 구간: [l, r]
    # 반으로 쪼갠 후 각각 구간의 승자를 구한 다음
    # - 왼쪽 구간: [l, mid] => 구간의 승자
    # - 오른쪽 구간: [mid+1, r] => 구간의 승자
    # 둘 중에서 최종 승자를 구하기

    mid = (l + r) // 2 # 가운데 학생 번호

    l_winner = winner(l, mid) # 왼쪽 구간의 승자의 번호를 재귀 호출로 구하기
    r_winner = winner(mid+1, r) # 오른쪽 구간의 승자의 번호를 재귀 호출로 구하기

    # cards[l_winner] : 왼쪽 구간의 승자의 가위바위보
    # cards[r_winner] : 오른쪽 구간의 승자의 가위바위보 숫자

    # 만약에 두 승자의 가위바위보가 같다면
    if cards[l_winner] == cards[r_winner]:
        return l_winner # 더 작은 승자 번호를 반환
    
    # 만약에 두 승자의 가위바위보가 다르다면, 
    # 가위바위보 결과에 따라 승자 번호 반환

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
    N = int(input()) # 학생 수, 번호 1번 ~ N번

    cards = [0] + list(map(int, input().split()))
    # N+1개의 리스트를 만들고 0번은 무시한다

    # 재귀함수(분할정복) 설계
    num = winner(1, N) # 1번부터 N번까지 모든 학생을 고려했을 때의 승자

    print(f"#{tc} {num}")

