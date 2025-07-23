T = int(input())  # 테스트 케이스 수

for tc in range(1, T + 1):
    N, K = map(int, input().split())  # 퍼즐 크기, 단어 길이
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    answer = 0  # 정답: 단어가 들어갈 수 있는 자리 수

    # ▶ 가로 방향 검사
    for i in range(N):
        row = [0] + puzzle[i] + [0]  # 앞뒤에 0 추가
        count = 0
        for j in range(len(row)):
            if row[j] == 1:
                count += 1  # 흰칸이면 개수 증가
            else:
                if count == K:
                    answer += 1  # 정확히 K칸이면 정답
                count = 0  # 0을 만나면 초기화

    # ▶ 세로 방향 검사
    for j in range(N):
        col = [0] + [puzzle[i][j] for i in range(N)] + [0]  # 앞뒤에 0 추가
        count = 0
        for i in range(len(col)):
            if col[i] == 1:
                count += 1
            else:
                if count == K:
                    answer += 1
                count = 0

    # ▶ 출력
    print(f"#{tc} {answer}")
