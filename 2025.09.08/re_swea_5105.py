# 5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리
'''
Queue를 활용한 2차원 배열

from collections import deque
에서 deque를만들고

- q를 만들고 방문처리 후, q에 시작점을 cnt와 집어넣기
- q가 있다면 꺼내서 탐색하자
    - q.popleft()를 통해 꺼내고
    - 4방 탐색 후, 값 == 0 and not visited이면 
        - q에 append하는데 level +1해서 추가
    - 3을 찾으면 종료 !
'''
