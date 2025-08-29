### 색종이 ###
# from pprint import pprint as print
N = int(input()) # N: 1~100
arr = [[0]*1000 for _ in range(1000)]
for paper in range(1, N+1): # N = 1, 2
    start_r, start_c, height, width = map(int, input().split()) # 0 0 10 10
    end_r, end_c = start_r + height, start_c + width

    for r in range(start_r, end_r): # r: 0~10
        for c in range(start_c, end_c): # c: 0~10
            arr[r][c] = paper

for paper in range(1, N+1): # N = 1, 2
    paper_cnt = 0
    for i in range(1000):
        for j in range(1000):
            if arr[i][j] == paper:
                paper_cnt += 1
    print(paper_cnt)


        


N = int(input())
arr = [[0]*1001 for _ in range(1001)]

for paper in range(1, N+1):
    x, y, w, h = map(int, input().split())
    for i in range(x, x+w):
        for j in range(y, y+h):
            arr[i][j] = paper

count = [0]*(N+1)

# 전체 평면 한 번만 순회
for i in range(1001):
    for j in range(1001):
        if arr[i][j] != 0:
            count[arr[i][j]] += 1

for paper in range(1, N+1):
    print(count[paper])
