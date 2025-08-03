# 알고리즘에서 def 쓰면 안되나? 이건 왜 안돼?
def reverse(n):
    if len(n) == 1:
        return n
    
    else:
        return n[-1] + reverse(n[:(len(n)-1)])

T = int(input())
for i in range(1, T+1):
    string = input()
    rev = reverse(string)
    if string == rev:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')



# T = int(input())
# for i in range(1, T+1):
#     string = input()
#     rev = string[::-1] # 역순으로 뒤집기
#     if string == rev:
#         print(f'#{i} 1')
#     else:
#         print(f'#{i} 0')