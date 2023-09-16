def nq(n, row, comb, result):
    if row == n:
        result[0] += 1
        return

    for col in range(n):
        is_valid = True
        for prev_row in range(row):
            if comb[prev_row] == col or \
               abs(comb[prev_row] - col) == abs(prev_row - row):
                is_valid = False
                break

        if is_valid:
            comb[row] = col
            nq(n, row + 1, comb, result)
            comb[row] = -1  # Backtrack

N = int(input())
result = [0]
nq(N, 0, [-1] * N, result)
print(result[0])
