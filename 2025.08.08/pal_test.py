# word = "aahoaaohba"
# n = len(word)
0# mid =  n // 2
#
# is_pal = True
# for i in range(mid): # 절반만큼만 돌기
#     print(word[i], word[n - 1 - i])
#     if word[i] != word[n-1-i]:
#         is_pal = False
#         break
#
# print(is_pal)

word = 'ahoha'
n = len(word)
mid = n//2
is_pal = True

for i in range(mid):
    if word[i] != word[n-1-i]:
        is_pal = False
        break
print((is_pal))