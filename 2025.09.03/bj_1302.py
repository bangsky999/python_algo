'''
N만큼 돌면서 들어오는걸 dict로 만들고 value를 1추가 
values에서 max값 찾기
'''
N = int(input())
nums = [0]*1000
name_list = []
for i in range(N):
    name = input()
    if name not in name_list: # 없으면 추가
        name_list.append(name) # 이름을 추가해라
    nums[name_list.index(name)] += 1
    
# name과 nums 정렬 완
max_num = -1
book_name = []
for i in range(len(name_list)):
    if nums[i] > max_num:
        max_num = nums[i]
        book_name.clear()
        book_name.append(name_list[i])
    elif nums[i] == max_num:
        book_name.append(name_list[i])

book_name.sort()
print(book_name[0])

