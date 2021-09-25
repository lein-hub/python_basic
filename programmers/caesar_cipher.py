def solution(s, n):
    ls = list(s)
    for i in range(len(ls)):
        if ls[i] == ' ':
            continue
        if ls[i].isupper():
            ls[i] = chr((ord(ls[i]) - ord('A') + n) % 26 + ord('A'))
        else:
            ls[i] = chr((ord(ls[i]) - ord('a') + n) % 26 + ord('a'))
    return ''.join(ls)
