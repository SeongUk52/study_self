#6056 : [기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기(설명)(py)

a, b = map(int, input().split())
c = bool(a)
d = bool(b)
print((c and not d) or (not c and d))