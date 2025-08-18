# score1, score2
# => 3개 분반으로 나누기
# min <= 각 분반의 학생 수 <= max
# 3개 분반 중에서 가장 많은 분반 - 가장 적은 분반의 차이가 최소값


# 최소값 : 완전 탐색 문제
# 모든 경우의 수를 전부 만든 다음 => 조건에 맞는 것들을 검사 => 그 중에서 최소값, 최대값 찾기
# 무식하게 전부 구하자(brute-force)

# 1 <= 점수(score1, score2) <= 100
T = int(input())

for tc in range(1, T+1):
    N, min, max = map(int, input().split())
    scores = list(map(int, input().split()))

    min_diff = 9999999 # 인원수 차이의 최소값.

    for score1 in range(1, 101):
        for score2 in range(score1, 101):
            # (score1, score2) 가능한 모든 조합 생성 (약 1만개)

            cls_cnt = [0]*3 
            #cls_cnt[0] 부진
            #cls_cnt[1] 보통
            #cls_cnt[2] 우수

            for score in scores:
                if score < score1:
                    cls_cnt[0] += 1
                elif score < score2:
                    cls_cnt[1] += 1
                else:
                    cls_cnt[2] += 1
            
            
            for i in range(3):
                if cls_cnt[i] < min or cls_cnt[i] > max: # 만약에 세 분반중에 하나라도 범위를 벗어났다면
                    break # 멈추기
            else: # for문을 돌면서 break 안만난 상황
                # 세 반 모두 다 범위 안에 있음. 여기서 검사
                # 세 분반의 최대 인원 - 최소 인원
                max_cnt = 0
                min_cnt = 9999999
                for i in range(3):
                    if cls_cnt[i] > max_cnt:
                        max_cnt = cls_cnt[i]
                    if cls_cnt[i] < min_cnt:
                        min_cnt = cls_cnt[i]
                diff = max_cnt - min_cnt
                if diff < min_diff:
                    min_diff = diff
    
    if min_diff == 9999999:
        print(f"#{tc} -1")
    else:
        print(f"#{tc} {min_diff}")