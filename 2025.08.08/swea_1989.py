import sys
sys.stdin = open("../input.txt")

# 방법 1 - 슬라이싱
T = int(input())
for tc in range(1, T+1):
    word = list(input())
    val = 0
    if word == word[::-1]:
        val = 1
    print(f'#{tc} {val}')



# 방법 2
T = int(input())
for tc in range(1, T+1):
    word = list(input())
    n = len(word)
    val = 1
    for i in range(n//2):
        if word[i] != word[n-i-1]:
            val = 0
    print(f'#{tc} {val}')