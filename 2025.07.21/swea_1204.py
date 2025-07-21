# 테스트 케이스 개수
T = int(input())

for _ in range(T):
    case_num = int(input())  # 케이스 번호
    scores = list(map(int, input().split()))  # 점수 리스트

    count = {i: 0 for i in range(101)}  # 0~100 점수 딕셔너리 초기화

    for score in scores:
        count[score] += 1  # 점수 등장 횟수 세기

    max_count = max(count.values())  # 가장 많이 나온 횟수
    most_common = [score for score, cnt in count.items() if cnt == max_count]
    answer = max(most_common)  # 가장 많이 나온 점수 중 가장 큰 것

    print(f"#{case_num} {answer}")
