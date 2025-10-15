# 햄버거 다이어트

def subset(arr, idx, current):
    if idx == len(arr):
        return

T = int(input())
for tc in range(1,T+1):
    N, L = map(int, input().split())
    hambur = [0]*N
    for i in range(N):
        T, K = map(int, input().split())
        hambur[i] = (T, K)

    
