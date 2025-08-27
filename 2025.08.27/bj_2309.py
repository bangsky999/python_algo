# import sys; sys.stdin = open("input.txt")
# height = [int(input()) for _ in range(9)]

# height.sort()
# G = sum(height) - 100 
# val = 0
# for i in range(8):
#     for j in range(9):
#         sub = height[:]
#         if sub[i] + sub[j] == G:
#             val = 1
#             sub.pop(i)
#             sub.pop(j-1)
#             for k in range(len(sub)):
#                 print(sub[k])
#         if val == 1:
#             break
#     if val == 1:
#         break

import sys; sys.stdin = open("input.txt")
height = [int(input()) for _ in range(9)]

val = 0
for i in range(8):
    for j in range(i+1, 9):
        sub = height[:]
        sub.pop(i)
        sub.pop(j-1)
        if sum(sub) == 100:
            sub.sort()
            for k in range(7):
                print(sub[k])
            val = 1
        if val == 1:
            break
    if val == 1:
        break