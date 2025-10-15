# 기타줄
'''
N: 기타줄, M: 브랜드
6개 패키지 가격, 낱개 살때 가격
'''
N, M = map(int, input().split()) # 끊어진 기타 줄 수 , 브랜드 수
sets = []
each = []

for i in range(M):
    s, e = map(int,input().split())
    sets.append(s)
    each.append(e)

sets_min = min(sets)
each_min = min(each)

result = 0 # 출력할것
# 낱개 가격(min) * 6이 sets의 min보다 작은 경우 이걸 쓰자
if each_min * 6 < sets_min:
    result = each_min * N

# 그렇지 않으면 set을 먼저 쓰고, 남은거는 sets의 min으로 채우자
else:
    aa = N//6
    if each_min * (N-(aa*6)) > sets_min:
        result = (aa+1) * sets_min
    else:
        result = aa * sets_min + each_min * (N-(aa*6))
# print(aa)
# print(sets_min)
# print(each_min)
# print(N-(aa*6))
print(result)