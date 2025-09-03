# 1. 부분집합의 수를 바로 구할 수 있다.
arr = [1,2,3,4]
print(1 << len(arr))

print('-----------------------------------')

# 2. 전체 부분집합을 구할 수 있다.
for i in range(1 << len(arr)):
    for idx in range(len(arr)):
        if i & (1 << idx):
            print(arr[idx], end = ' ')
    print()

print('-----------------------------------')

# 3. 응용 - 합이 10인 부분집합만 구해라
arr = [1,2,3,4,5,6]
for i in range(1 << len(arr)):
    subset = []
    total = 0

    for idx in range(len(arr)):
        if i & (1 << idx):
            subset.append(arr[idx])
            total += arr[idx]

    if total == 10:
        print(subset)