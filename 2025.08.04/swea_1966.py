T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort() # arr = [0,1,4,7,8]
    print(f"#{tc}", end=' ')
    for i in arr:
        print(i, end = ' ')
    print()

"""

print("Hello", end='\n') : "Hello"출력하고 그다음 줄로 넘어감
print("Hello", end='') : 그 다음줄로 안넘어감

"""