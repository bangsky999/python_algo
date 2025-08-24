N = int(input()) # 26
cnt = 0
a = str(N)
while True: # N이 re_N이 될때까지
    # '55'
    if int(a) < 10: # '07' // '1'
        a = '0'+str(int(a))
    b = str(int(a[0])+int(a[1])) # '26'
    if int(b) < 10:
        b = '0'+str(int(b)) # '08'

    a = a[1] + b[1] # '68'
    cnt += 1
    if str(N) == str(int(a)):
        break

print(cnt)
