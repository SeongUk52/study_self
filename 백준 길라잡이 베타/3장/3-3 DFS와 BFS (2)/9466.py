import sys
sys.setrecursionlimit(100001)

def dfs(node, graph, visited, team):
    if visited[node]:  # 이미 방문한 노드를 만났을 때
        if node in team:  # 사이클의 시작점을 찾았을 때
            return team.index(node)  # 사이클의 시작점부터 리스트의 끝까지가 사이클
        return -1  # 이미 방문한 노드이지만 사이클 시작점이 아닐 때

    visited[node] = True
    team.append(node)
    next_node = graph[node]
    return dfs(next_node, graph, visited, team)


t = int(input())
for _ in range(t):
    n = int(input())
    graph = [0] + list(map(int, sys.stdin.readline().split()))
    cnt = 0
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            team = []  # 팀에 속한 노드들을 리스트로 관리
            cycle_start_idx = dfs(i, graph, visited, team)
            if cycle_start_idx != -1:
                cnt += len(team) - cycle_start_idx  # 사이클의 시작점부터 리스트의 끝까지가 사이클
    print(n-cnt)
