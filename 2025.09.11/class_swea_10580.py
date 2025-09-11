# 전봇대
'''
최초 입력에는 선이 교차점이 안생긴다
1. 교차점을 모두 빈 리스트에 저장하고
2. 새로운 전봇대가 들어오면 이전의 모든 전봇대 줄과 비교를 해서 교차점을 count한다
    - 이전의 전봇대와 비교하기
        - 새로들어온 시작점이 기존보다 작고 끝점이 기존보다 큰 경우
        - 새로들어온 시작점이 기존보다 크거나 끝점이 기존보다 작은 경우
    - 비교 case 마다 cnt올리기
시작 cnt = 0
'''
import sys;sys.stdin=open("input.txt")

T = int(input()) 
for tc in range(1,T+1):
    N = int(input())
    
    cnt = 0 # 교차점의 수

    wires = [] # 전봇대를 저장할 빈리스트
    for wire in range(N): # N번 반복
        wire_start, wire_end = map(int,input().split()) # 1, 10

        if not wires: # 초기 없을 떄만 추가
            wires.append((wire_start,wire_end))
            continue

        # 검사 후 추가
        for i in wires: # wires를 순회하며 시작점 , 끝점 비교
            if wire_start < i[0] and wire_end > i[1]:
                cnt += 1
            if wire_start > i[0] and wire_end < i[1]:
                cnt += 1
        
        # wires에 비교 후 추가  
        wires.append((wire_start,wire_end))

    print(f'#{tc} {cnt}')
