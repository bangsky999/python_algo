n = int(input())

all_list = []

for i in range(1,n+1):
    if n % i == 0:
        all_list.append(i)

for num in all_list:
    print(num, end = ' ')