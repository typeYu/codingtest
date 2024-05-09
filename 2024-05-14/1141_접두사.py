"""
1141. 접두사

['h', 'hi', 'xi', 'hio', 'run', 'hcc', 'hipo', 'runn', 'runc', 'runni', 'running']

'h' -> 'hi', 'hio', 'hipo' 제거
'hi' -> 'hio', hipo' 제거
'xi' -> x
'hio' -> x
'run' -> 'runn', 'runc', 'runni' 제거
'hcc' -> x
'hipo' -> x
'runn' -> 'running' 제거
'runc' -> x
'runni' -> 'running' 제거
'running' -> 'x'
"""
N = int(input())
words = [input().strip() for _ in range(N)]

words.sort(key=len)
answer = 0

for idx, word in enumerate(words):
    l = len(word)
    is_prefix = False

    for other in words[idx+1:]:
        if word == other[:l]:
            is_prefix = True
            break

    if not is_prefix:
        answer += 1

print(answer)