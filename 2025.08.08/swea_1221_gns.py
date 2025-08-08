'''
딕셔너리를 두개 쓰자 sort를 쓰자
'''
import sys
sys.stdin = open("../input.txt")

dict1 = {0: 'ZRO',1: 'ONE',2: 'TWO', 3: 'THR', 4: 'FOR', 5: 'FIV', 6: 'SIX', 7: 'SVN', 8: 'EGT', 9: 'NIN'}
dict2 = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

T = int(input())
for tc in range(1, T+1):
    trash = input()
    order = list(input().split())
    lst = []
    lst = [dict2[i] for i in order]
    lst.sort()
    lst1 = [dict1[i] for i in lst]
    print(f'#{tc}')
    print(' '.join(lst1))

