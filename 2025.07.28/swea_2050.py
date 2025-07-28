lst = input()
# ord('A') 함수 사용할 것
for i in lst:
    print(ord(i) - ord('A') + 1 ,end = ' ')