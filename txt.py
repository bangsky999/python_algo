def per(idx):
    # 종료 조건 : 모든 자리를 채운 경우
    if idx == N:
        print(*arr) # 채워진 순열을 출력
        return
    
    # 유도조건 : idx 번째 자리에 아직 안쓴 숫자를 넣기
    for i in range(N): # i는 0 ~ N-1
        if not visited[i]: # i번째 숫자를 아직 사용하지 않았다면,
            visited[i] = True # visited 채우기
            arr[idx] = i+1 # 
            per(idx+1)
            visited[i] = False
N = int(input()) # 입력 받기
arr = [0]*N # 결과를 담을 배열 (순열 저장용)
visited = [False]*(N+1) # 방문처리 배열
per(0) # 재귀 시작