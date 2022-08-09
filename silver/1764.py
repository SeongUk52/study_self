N, M = input().split()
N = int(N)
M = int(M)

cannotHS = [""]*(N+M)
dbj = []

for i in range(N+M):
    cannotHS[i] = input()
cannotHS.sort()
for i in range(len(cannotHS)-1):
    if cannotHS[i] == cannotHS[i+1]:
        dbj.append(cannotHS[i])
print(len(dbj))
for i in dbj:
    print(i)