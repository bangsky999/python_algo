T = int(input())
 
 
def delete_repetition(text):
    found = False
    idx = -1
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            found = True
            idx = i
            break
 
    if found:
        return delete_repetition(text[:idx]+text[idx+2:])
    else:
        return text
 
 
for tc in range(1, T+1):
    text = input().strip()
 
    # ans = delete_repetition(text)
    print(f"#{tc} {len(delete_repetition(text))}")