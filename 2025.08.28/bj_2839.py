### 설탕 배달 ###
'''
DFS인가?DPS인가? 끝까지 가다가 값이 0보다 작아지면 -5 대신 -3 하고 체크
(재귀함수인가?)
언제까지 할지 모르니까 while
answer -> 재귀/백트래킹(dfs)로 -> 끝까지 가보다가 안되면 다른 경로 시도
'''
# ### dfs(재귀) 풀이
# N = int(input())
# ans = float('inf')

# def dfs(num,cnt): # num, cnt를 받겠다.
#     global ans
#     # 성공 케이스
#     if num == 0:
#         ans = min(ans, cnt)
#         return
#     # 실패 케이스
#     if num < 0:
#         return
#     # 분기(5를쓸지 3을쓸지)
#     dfs(num - 5, cnt + 1)
#     dfs(num - 3, cnt + 1)

# dfs(N,0)
# print(-1 if ans == float('inf') else ans)
    


# ### 그리디 풀이
# N = int(input())

# ans = -1
# # 5kg를 최대한 많이 쓰면서, 남는 무게가 3으로 나누어 떨어지는지 확인
# for five in range(N // 5, -1, -1):
#     rest = N - 5 * five
#     if rest % 3 == 0:
#         three = rest // 3
#         ans = five + three
#         break
# print(ans)


### DFS -> 3<=N<=5000이기에 가능하진않음
N = int(input())
min_cnt = float('inf')
def dfs(num, cnt):
    global min_cnt
    if num == 0: # 값이 딱 맞으면
        if cnt < min_cnt:
            min_cnt = cnt
            return
    if num < 0:
        return # 이 경우는 보지 않겠다
    if cnt > min_cnt:
        return # 가지치기
    else:
        dfs(num-5, cnt+1)
        dfs(num-3, cnt+1)
dfs(N,0)
if min_cnt == float('inf'):
    print(-1)
else:
    print(min_cnt)





# ### DP(다이나믹 프로그래밍)
# N = int(input())
# dp = [0]*(5001)

# # 우리가 알고 있는 최소한의 상태를 적을 것
# dp[1] = -1
# dp[2] = -1
# dp[3] = 1
# dp[4] = -1
# dp[5] = 1

# # dp의 1~5번까지는 알고있으니 문제의 6~5000번까지 로직을 짜자!
# for n in range(6, 5001):
#     # dp의 n-3, n-5 값이 -1이 아니면 그전까지 계산값의 최소값에 +1하겠다.
#     if dp[n-3] != -1 and dp[n-5] != -1:
#         dp[n] = min(dp[n-3], dp[n-5]) + 1
#     elif dp[n-3] != -1:
#         dp[n] = dp[n-3] + 1
#     elif dp[n-5] != -1:
#         dp[n] = dp[n-5] + 1
#     else:
#         dp[n] = -1

# print(dp[N])




# ### 그리디
# N = int(input())
# cnt = 0
# while True:
#     if N % 5 ==0: # 한번에 나온다
#         print(cnt + N//5)
#         break
#     N -= 3
#     cnt += 1
#     if N == 0:
#         break
#     if N <= -1:
#         cnt = -1
#         break       
# print(cnt)

