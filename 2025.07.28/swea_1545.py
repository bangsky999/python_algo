N = int(input())
# lst = list(range(0, N+1)) => [0,1,2,3, ...N]
lst = list(range(0, N+1))
lst.reverse() # 리스트.reverse() 뒤집기
for i in lst:
    print(i, end = ' ')
    
