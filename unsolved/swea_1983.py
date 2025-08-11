import sys
sys.stdin = open("input.txt")
## 조교의 성적정리
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total_list = []
    for s in arr:
        score = s[0]*0.35 + s[1]*0.45 + s[2]*0.2
        total_list.append(score)
    print('1', total_list)
    print()
    stu_dict = {}
    for i in range(1,N+1):
        stu_dict[i] = total_list[i-1]
    print('s_dict', stu_dict)
    print()
    total_list.sort(reverse=True)
    print('2', total_list)
    # grade = ''
    # num = total_list.index(stu_dict[K])
    # if (num // 2)//(N//10) == 0 allnd (num // 2)%(N//10) == 0:
    #     grade = 'A+'
    # elif (num // 2)//(N//10) == 0 and (num // 2)%(N//10) == 1:
    #     grade = 'A0'
    # elif (num // 2)//(N//10) == 1 and (num // 2)%(N//10) == 0:
    #     grade = 'A-'
    # elif (num // 2)//(N//10) == 1 and (num // 2)%(N//10) == 1:
    #     grade = 'B+'
    # elif (num // 2)//(N//10) == 2 and (num // 2)%(N//10) == 0:
    #     grade = 'B0'
    # elif (num // 2)//(N//10) == 2 and (num // 2)%(N//10) == 1:
    #     grade = 'B-'
    # elif (num // 2)//(N//10) == 3 and (num // 2)%(N//10) == 0:
    #     grade = 'C+'
    # elif (num // 2)//(N//10) == 3 and (num // 2)%(N//10) == 1:
    #     grade = 'C0'
    # elif (num // 2)//(N//10) == 4 and (num // 2)%(N//10) == 0:
    #     grade = 'C-'
    # elif (num // 2)//(N//10) == 4 and (num // 2)%(N//10) == 1:
    #     grade = 'D0'
    
    # print(f'#{tc} {grade}')