'''
stack 리스트를 만들고 
push -> append
pop -> pop
size -> len
empty -> len : 0
top : print -1, 비어있으면 -1
'''
from collections import deque

N = int(input())
stack = deque()
for i in range(N):
    command = input().split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print('-1')
    elif command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print('-1')
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if stack:
            print('0')
        else:
            print('1')