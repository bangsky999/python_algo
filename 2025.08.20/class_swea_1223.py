### 계산기2 ###

T = 10 # 테스트케이스 10개 고정

for tc in range(1, T+1):
    N = int(input()) # 문자열의 길이(중위표현식)
    exp = input() # 중위표현식
    out = '' # 후위표기식을 저장할 변수

    # exp = "9+5*2+1+3*3*7*6*9*1*7"

    # Step 1. 중위표기식 => 후위표기식으로 변환하기
    #  - 연산자의 우선순위를 정렬하는 것
    #  - 연산자의 스택을 사용

    # 규칙
    # exp를 왼쪽부터 오른쪽으로 가면서 한 문자(c)씩 검사
    # 1. c가 피연산자라면 => out에 그대로 출력(후위표기식에 이어붙임)
    # 2. c가 연산자라면
    #    2.1. 스택이 비어있다면 => c를 스택에 push
    #    2.2. 스택이 비어있지 않다면 => 스택의 top과 c를 비교
    #         2.2.1. top의 우선순위가 낮다면 => c를 스택에 push
    #         2.2.2. top의 우선순위 == c의 우선순위 => 먼저 스택에 들어있는 것이 더 우선 => top을 꺼내서 출력한 후, c를 push
    #         2.2.3. top의 우선순위가 더 높다면 => c보다 우선순위가 높거나 같은 것들을 전부 pop해서 출력 => c를 push
    # 3. 검사가 다 끝났으면, 마지막에는 스택을 비워준다.

    stack = [] # 연산자의 스택

    for c in exp: # 중위표기식에서 왼쪽부터 오른쪽으로 한 문자(c)씩 검사
        if c == '*': # 우선순위 높은 연산자
            if not stack: # 스택이 비어있다면
                stack.append(c)
            elif stack[-1] == '+': # 스택이 비어있지 않고, top이 '+'라면
                stack.append(c)
            else: # 우선순위 같은 경우
                while stack and stack[-1] == '*': # 스택에 있는 것을 먼저 꺼내서 출력
                    out += stack.pop() # 스택에 있는 것을 먼저 꺼내고
                stack.append(c) # 현재 c 그다음에 스택에 추가
        
        elif c == '+':
            while stack: # 스택에 뭔가가 있다면, 스택에 있는 것이 현재 연산자보다 우선순위가 높음
                out += stack.pop()
            stack.append(c)
        
        else: # 피연산자라면
            out += c
    
    # 검사가 끝나고 스택을 전부 비워준다.
    while stack:
        out += stack.pop()


    # Step 2. 후위표기식 계산하기
    # - 숫자의 스택 사용
    
    stack2 = [] # 숫자의 스택
    # 스택에서 가장 최근의 두개의 숫자를 꺼내서 계산한다음, 계산 결과를 다시 스택에 넣는다
    # 왼쪽 -> 오른쪽 순서로 한 문자씩 본다
    # 피연산자라면 => 스택에 넣는다.
    # 연산자라면 => 스택에서 두 개 꺼내서 계산한다음 다시 스택에 넣는다

    for c in out:
        if '0' <= c <= '9': # 만약에 문자 c가 숫자문자라면
            stack2.append(int(c)) # 숫자의 스택에 정수로 변환해서 push
        elif c == '+':
            num1 = stack2.pop()
            num2 = stack2.pop()
            stack2.append(num1+num2)
        elif c == '*':
            num1 = stack2.pop()
            num2 = stack2.pop()
            stack2.append(num1*num2)
    
    # 계산 후 스택에 마지막에 들어있는 숫자가 계산 결과
    print(f"#{tc} {stack2.pop()}")