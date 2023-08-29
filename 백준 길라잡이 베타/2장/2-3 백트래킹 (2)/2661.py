def is_good_sequence(seq, length):
    for l in range(1, length // 2 + 1):
        if seq[-l:] == seq[-2 * l:-l]:
            return False
    return True

def bt(n, comb, result):
    if len(comb) == n:
        result.append(comb[:])
        return

    if result:
        return  # 이미 좋은 수열을 찾은 경우 종료
    for i in range(1, 4):
        if comb and comb[-1] == i:
            continue

        new_comb = comb + [i]
        if is_good_sequence(new_comb, len(comb) + 1):
            bt(n, new_comb, result)

n = int(input())
result = []
bt(n, [], result)
print(''.join(map(str, result[0])))
