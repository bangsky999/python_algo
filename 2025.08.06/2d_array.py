arr = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       ]


# # 델타 배열
# # 특정한 좌표 (r,c)를 중심으로 상하좌우, 대각선 탐색을 하고 싶은 경우,
# # ex) 칸의 숫자가 6이면, 상하좌우에 있는 칸에다가 +10을 하겠다.
# dr = [1,-1,0,0]
# dc = [0,0,1,-1]

# for r in range(3):
#     for c in range(4):
#         if arr[r][c] == 6:
#             for d in range(4):
#                 nr, nc = r+dr[d], c+dc[d]

#                 if 0<=nr<3 and 0<=nc<4:
#                     arr[nr][nc] += 10

    
# for r in range(3):
#     for c in range(4):
#         print(arr[r][c], end = ' ')

#     print()

# # 대각선 배열
# dr = [-1,-1,1,1]
# dc = [-1,1,1,-1]

# for r in range(3):
#     for c in range(4):
#         if arr[r][c] == 6:
#             for d in range(4):
#                 nr, nc = r+dr[d], c+dc[d]

#                 if 0<=nr<3 and 0<=nc<4:
#                     arr[nr][nc] += 10

# for r in range(3):
#     for c in range(4):
#         print(arr[r][c], end = ' ')

#     print()



# # 상하좌우 대각선 배열
# dr = [-1,-1,1,1] + [1,-1,0,0]
# dc = [-1,1,1,-1] + [0,0,1,-1]
# for r in range(3):
#     for c in range(4):
#         if arr[r][c] == 6:
#             for d in range(8):
#                 nr, nc = r+dr[d], c+dc[d]

#                 if 0<=nr<3 and 0<=nc<4:
#                     arr[nr][nc] += 10

# for r in range(3):
#     for c in range(4):
#         print(arr[r][c], end = ' ')
#     print()


# # 델타 응용
# max_v = 0
# for i in range(N):
#     for j in range(N):
#         s = arr[i][j]
#         for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
#             for c in range(1, 3):
#                 ni, nj = i+c*di, j+c*dj
#                 if 0<=ni<N and 0<=nj<N:
#                     s += arr[ni][nj]

#         if max_v < s:
#             max_v = s