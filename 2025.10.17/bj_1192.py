N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0 # 부분순열의 개수
# 비트마스킹 처리
for i in range(1, 1<<N): # i를 1~ (2^5-1) 2진수로 표현, 공집합은 제외
    total = 0
    for j in range(N): # j는 0~4까지 5칸을 체크할거니까
        if i & (1<<j): # j를 하나씩 시프트했을때 이진수표현 i와 둘다 1이라면 => 값이 존재한다면
            total += arr[j]
    if total == S:
        cnt += 1
print(cnt)