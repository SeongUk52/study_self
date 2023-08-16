import heapq
A,B = map(int,input().split())
INF = 1e9

distance = [INF] * (B+1)

def dijkstra(start,end):
    q = []
    heapq.heappush(q,(1,start))
    distance[start] = 1

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        if now*2 <= end:
            if dist+1 < distance[now*2]:
                distance[now*2] = dist+1
                heapq.heappush(q,(dist+1,now*2))

        if now*10+1 <= end:
            if dist+1 < distance[now*10+1]:
                distance[now*10+1] = dist+1
                heapq.heappush(q,(dist+1,now*10+1))

dijkstra(A,B)
if distance[-1] == INF:
    print(-1)
else:
    print(distance[-1])