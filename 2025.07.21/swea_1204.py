T = int(input())

for _ in range(T):
    num_test = int(input())
    test_case = list(map(int, input().split()))

    #count 끝~
    count = {}

    for i in test_case:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    # key, value 저장 변수 만들기
    max_count = 0
    answer = 0

    for key in count:
        if count[key] > max_count:
            max_count = count[key]
            answer = key
        elif count[key] == max_count and key > answer:
            answer = key

    print(f"#{num_test} {answer}")

