'''
증가하는 point를 만들고 싶다 => 맨뒤는 건들지 말고
그 앞은 맨뒤 수보다 크거나 같으면 맨뒤 -1까지 줄이자
그 앞도 반복
그 앞도 반복
...
뺄때마다 reduce_score += 1
'''
N = int(input())
clear_scores = [int(input()) for _ in range(N)]
level = N-2
reduce_score = 0
while level != -1:
    if clear_scores[level] >= clear_scores[level+1]:
        reduce_score += (clear_scores[level] - clear_scores[level+1] + 1)
        clear_scores[level] = clear_scores[level+1] - 1
        
    level -= 1
print(reduce_score)