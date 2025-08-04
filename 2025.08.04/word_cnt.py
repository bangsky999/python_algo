arr = [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1]

cnt = 0
for i in range(len(arr)):
    if arr[i] == 1:
        cnt += 1
    else:
        print(f"cnt: {cnt}")
        cnt = 0
    
    if i == len(arr) - 1:
        print(f"cnt: {cnt}")



# arr = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# N = 3
# for r in range(N):
#     for c in range(N):
#         print(arr[r][c], end=' ')
#     print()


# for r in range(N):
#     for c in range(N):
#         print(arr[c][r], end=' ')
#     print()
