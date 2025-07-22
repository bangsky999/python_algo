T = int(input())
for i in range(1, T+1):
    N = int(input())
    chart = list(map(int, input().split()))
    # 왜 None이 나올까?? -> sort함수의 return 값은 None
    # 그럼 어떻게 해결?? -> chart.sort()로 정렬하고 그냥 chart쓰기
    chart.sort()
    
    # map(str, nums)는 리시트의 모든 숫자들을 문자열로 바꾸기
    # 문자열 리스트를 ' '(공백)을 기준으로 한 줄로 붙이기
    result = ' '.join(map(str, chart))
    print(f"#{i} {result}")
