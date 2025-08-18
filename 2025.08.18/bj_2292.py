### 벌집 미완 ### 수정바람

T = int(input())

n = 1 # 층 수
max_num = 1 # 마지막 방 번호

while T > max_num:
    max_num += 6 * n
    n += 1

print(n)
