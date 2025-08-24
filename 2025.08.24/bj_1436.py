### 영화감독 숌 ###
'''
666부터 +=1 씩 증가시키는데 666이 순회하다 666이 있으면 cnt += 1하고 ex. 666검사했고 cnt가 입력값디 딱되면
값을 출력하자
'''
num = 665
N = int(input()) # 1
cnt = 0
while True:
    num += 1 # 666
    cnt_6 = 0
    
    if '666' in str(num):
        cnt += 1
    
    if cnt == N:
        print(num)
        break

