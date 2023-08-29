def chiDist(m,graph,chick):
    result = []
    for i in chick:
        sumdist = 0
        for j in range(m):
            for k in range(m):
                if graph[j][k] == 1:
                    mini = float('infinity')
                    for x in i:
                        dist = abs(j-x[0])+abs(k-x[1])
                        if dist<mini:
                            mini = dist
                    sumdist += mini
        result.append(sumdist)
    print(min(result))
def bt(x, y, n, m, graph, comb, result):
    if len(comb) == m:
        result.append(comb[:])
        return

    for i in range(x, n):
        start_y = y if i == x else 0
        for j in range(start_y, n):
            if graph[i][j] == 2 and not any(c == [i, j] for c in comb):
                comb.append([i, j])
                bt(i, j + 1, n, m, graph, comb, result)
                comb.pop()

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
chick = []
bt(0, 0, n, m, graph, [], chick)
chiDist(n,graph,chick)


