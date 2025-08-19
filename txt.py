arr = [1,2,3,4,5]

# 부분집합
# - 각 원소를 포함할 것인가? 포함하지 않을 것인가?
# - 비트마스킹(0 or 1)

N = len(arr)
out = [False]*N # 출력배열(해당 위치 포함 여부)

def f(idx):
    # 기저조건
    if idx == N: 
        for i in range(N):
            if out[i]:
                print(arr[i], end = ' ')
        print()
        return
    
    # 유도조건 (N-1)까지는 뽑을지 말지 결정가능.
    out[idx] = True # idx번째 부분집합에 포함시키고 
    f(idx+1) # idx+1 번째 결정하러 가기
    out[idx] = False # idx번쨰를 포함시키지 말고
    f(idx+1) # idx+1 번째 결정하러 가기

f(0)