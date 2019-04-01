import sys
import collections

n, m = map(int, input().split())
position = [list(map(int, input().split())) for _ in range(n)]
wall = [(x, y) for x in range(n) for y in range(m) if position[x][y] == 0]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0


# 감영시키는 것
def dfs(now_x, now_y, Map):
    for _ in range(4):
        next_x = now_x + dx[_]
        next_y = now_y + dy[_]
        if next_x >= 0 and next_x < n and next_y >= 0 and next_y < m:
            if Map[next_x][next_y] == 0:
                Map[next_x][next_y] = Map[now_x][now_y]
                dfs(next_x, next_y, Map)


def bfs():
    while q:
        now_x, now_y = q.popleft()
        for _ in range(4):
            next_x = now_x + dx[_]
            next_y = now_y + dy[_]
            if next_x >= 0 and next_x < n and next_y >= 0 and next_y < m:
                if Map[next_x][next_y] == 0:
                    Map[next_x][next_y] = Map[now_x][now_y]
                    q.append((next_x, next_y))

#이제 막는거(벽 3개 두는 모든 경우) 경우의 수 -- for문 3개가 핵심!
## 처음 position은 두고, 임시로 벽을 세운 맵을 a = b로 가져올 경우 call by reference로 가져오기때문에 처음 position이 변한다.
### 따라서 값만 가져오는 call by value만 해서 값만 가져와야한다!!
for i in range(len(wall)):
    for j in range(i+1, len(wall)):
        for k in range(j+1, len(wall)):
            ## 벽세우기(3개) -- call by value
            Map = [[0 for _ in range(m)] for _ in range(n)]
            for x in range(n):
                for y in range(m):
                    Map[x][y] = position[x][y]
            Map[wall[i][0]][wall[i][1]] = 1
            Map[wall[j][0]][wall[j][1]] = 1
            Map[wall[k][0]][wall[k][1]] = 1
            # 감영시키기 - DFS
            # for x in range(n):
            #     for y in range(m):
            #         if Map[x][y] == 2:
            #             dfs(x, y, Map)
            # 감영시키기 - BFS
            for x in range(n):
                for y in range(m):
                    if Map[x][y] == 2:
                        q = collections.deque()
                        q.append((x, y))
                        bfs()
            ## 안전한 구역 세기
            temp_cnt = 0
            for x in range(n):
                for y in range(m):
                    if Map[x][y] == 0:
                        temp_cnt += 1
            ## 기존의 것과 비교
            cnt = max(cnt, temp_cnt)
print(cnt)
