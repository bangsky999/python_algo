arr = [1, 2, 3]
n = len(arr)

for i in range(1 << n):  # 0부터 7까지 (부분집합의 수)
    subset = []
    for j in range(n):
        if i & (1 << j):  # j번째 원소가 포함되어 있는지 확인
            subset.append(arr[j])
    print(subset)
