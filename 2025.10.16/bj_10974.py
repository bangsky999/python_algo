def per(idx):
    if idx == N:
        print(*arr)
        return
    # 유도조건 - 아직 채워야할 결과 배열이 남았다면,
    for i in range(N): # 0부터 N-1 까지 ,,, i = 0일때
        if not visited[i]: # 0을 방문하지 않았다면
            visited[i] = True # 방문처리
            arr[idx] = i+1 # 출력할 배열 채우기
            per(idx+1) # 다음 배열 채우기 
            # 다채우고 돌아왔다면
            visited[i] = False
            
N = int(input()) # 입력 받기
arr = [0]*N # 출력할 결과 배열
visited = [False]*N # 방문 처리 배열
per(0)