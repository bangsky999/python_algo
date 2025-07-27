# map 함수 - 반복 가능한 데이터 구조의 모든 요소에 function을 적용하고, 그 결과 값들을 
# map object로 묶어서 반환
# map(function, iterable)

# zip 함수 - 반복 가능한 데이터 구조를 묶어서, 같은 위치에 있는 값들을 하나의 tuple로 만든 뒤 
# 그것들을 모아 zip object로 반환하는 함수

# girls = ['jane', 'ashley']
# boys = ['peter', 'jay']
# pair = zip(girls, boys)

# print(list(pair))

# names = ['철수', '영희', '민수']
# scores = [80,90,100]

# for name, score in zip(names, scores):
#     print(name, score)

# <for-else>
# for문 뒤에 붙는 else는 반복문이 중간에 break 없이 끝났을 때만 실행.
# 무언가를 찾는 루프에서 조건에 맞는 것을 못 찾았을 때 실행하는 코드를 짜고 싶을 때

# registered_ids = ['admin', 'user01', 'guest', 'user02']
# id_to_check = 'gu1est' # 이미 리스트에 존재하는 아이디
# for existing_id in registered_ids:
#     if existing_id == id_to_check:
#         print('이미 사용 중인 아이디입니다.')
#         break # 중복 아이디를 찾았으므로 확인 절차를 중단
# else:
#     # for 루프가 break로 중단되었기에 이 부분은 실행되지 않음
#     print('사용 가능한 아이디입니다.')
# print('아이디 확인 절차를 종료합니다.')


# <enumerate>
# 반복하면서 인덱스와 값을 동시에 꺼내주는 함수
# fruits = ['사과', '바나나', '포도']

# for idx, fruit in enumerate(fruits):
#     print(idx, fruit)

# movies = ['인터스텔라', '기생충', '인사이드 아웃', '라라랜드']

# for idx, title in enumerate(movies, start=1):
#     print(idx, title)

# 인덱스 정보를 이용해 요소의 위치를 확인할 수 있음
respondents = ['은지', '정우', '소민', '태호']
answers = ['', '좋아요', '', '괜찮아요']

for i, response in enumerate(answers):
    if response == '':
        print(f'{respondents[i]} 미제출')