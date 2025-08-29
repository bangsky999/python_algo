### 창고 다각형 ###
'''
입력을 받자
N을받자
L, H를 받으면 L을 순서대로 정렬하고 싶네??
정렬한뒤 왼쪽부터 가면서 블록을 만들자 [0]*1001 만들고
1. 제일 높은 H값을 찾자
큰 H를 기준으로
2. 좌측이 떨어지는 계단이면 떨어지기 전 블록으로 유지, 오르는 계단이면 계단대로 넓이 계산
3. 우축이 떨어지는 계단이면 떨어지는 대로 넓이 계산, 오르는 계단이면 오른 계단으로 최신화
'''
N = int(input())
building = [0]*1001

for i in range(N):
    L, H = map(int, input().split())
    building[L] = H

# print(building[:20]) # [0, 0, 4, 0, 6, 3, 0, 0, 10, 0, 0, 4, 0, 6, 0, 8, 0, 0, 0, 0]
high, idx = max(building), building.index(max(building)) # 10 8
roof_l = 0
roof_r = 0
for i in range(0, idx): # 정방향 순회
    if roof_l <= building[i]: # building이 크면 roof를 최신화, buiding을 그대로 따르겠다
        roof_l = building[i]
    else: # 작으면 그 빌딩에 roof를 덮어쓰겠다
        building[i] = roof_l


for i in range(1000,idx,-1):
    if roof_r <= building[i]:
        roof_r = building[i]
    else: 
        building[i] = roof_r

# print('---')
# print(building[:20])

print(sum(building))