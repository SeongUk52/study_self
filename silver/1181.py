N = int(input())
str = [""] * N
lenS = [0] * N
for i in range(N):
    str[i] = input()
for i in range(len(str)):
    lenS[i] = len(str[i])
for i in range(len(lenS) - 1):
    for j in range(i+1, len(lenS)):
        if (lenS[i] > lenS[j]):
            temp = lenS[i]
            lenS[i] = lenS[j]
            lenS[j] = temp
            temp = str[i]
            str[i] = str[j]
            str[j] = temp
        elif (lenS[i] == lenS[j] and str[i] > str[j]):
            temp = str[i]
            str[i] = str[j]
            str[j] = temp

print(str[0])
for i in range(1, len(str)):
    if (str[i] == str[i-1]):
        continue
    print(str[i])