# import sys; sys.stdin = open("input.txt")

T = 10
div_set = set()
for i in range(T):
    
    N = int(input())
    div_set.add(N % 42)

print(len(div_set))
