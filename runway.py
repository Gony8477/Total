import sys

N, L = map(int, sys.stdin.readline().split())
Map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def dfs_x(now_x, now_y, cnt):
    if now_y == N-1:
        cnt += 1
        return cnt
    else:
        next_y = now_y + 1

        if next_y >= 0  and next_y < N:
            ## 같은 높이인경우
            if Map[now_x][next_y] == Map[now_x][now_y]:
                cnt = dfs_x(now_x, next_y, cnt)
            ## 다음 지점이 더 높은 경우
            if Map[now_x][next_y] > Map[now_x][now_y]:
                if next_y - L >= 0:
                    for back in range(L):
                        if Map[now_x][now_y - back] == (Map[now_x][next_y] - 1) and dp[now_x][now_y - back] != 1:
                            dp[now_x][now_y - back] = 1
                            if back == L-1:
                                cnt = dfs_x(now_x, next_y, cnt)
                            continue
                        break
            ## 다음 지점이 더 낮은 경우
            if Map[now_x][next_y] < Map[now_x][now_y]:
                if now_y + L < N:
                    for foward in range(L):
                        if Map[now_x][next_y + foward] == (Map[now_x][now_y] - 1) and dp[now_x][next_y + foward] != 1:
                            dp[now_x][next_y + foward] = 1
                            if foward == L-1:
                                cnt = dfs_x(now_x, next_y, cnt)
                            continue
                        break
    return cnt

def dfs_y(now_x, now_y, cnt):
    if now_x == N-1:
        cnt += 1
        return cnt
    else:
        next_x = now_x + 1

        if next_x >= 0  and next_x < N:
            ## 같은 높이인경우
            if Map[next_x][now_y] == Map[now_x][now_y]:
                cnt = dfs_y(next_x, now_y, cnt)
            ## 다음 지점이 더 높은 경우
            if Map[next_x][now_y] > Map[now_x][now_y]:
                if next_x - L >= 0:
                    for back in range(L):
                        if Map[now_x - back][now_y] == (Map[next_x][now_y] - 1) and dp[now_x- back][now_y] != 1:
                            dp[now_x - back][now_y] = 1
                            if back == L-1:
                                cnt = dfs_y(next_x, now_y, cnt)
                            continue
                        break
            ## 다음 지점이 더 낮은 경우
            if Map[next_x][now_y] < Map[now_x][now_y]:
                if now_x + L < N:
                    for foward in range(L):
                        if Map[next_x + foward][now_y] == (Map[now_x][now_y] - 1) and dp[next_x + foward][now_y] != 1:
                            dp[next_x + foward][now_y] = 1
                            if foward == L-1:
                                cnt = dfs_y(next_x, now_y, cnt)
                            continue
                        break
    return cnt

cnt_x = 0
dp = [[0 for _ in range(N)] for _ in range(N)]
# 행에서 가는 길 수 보기
for x in range(N):
    cnt_x = dfs_x(x, 0, cnt_x)
#print(cnt_x)

cnt_y = 0
dp = [[0 for _ in range(N)] for _ in range(N)]
# 열에서 가는 길 수 보기
for y in range(N):
    cnt_y = dfs_y(0, y, cnt_y)
#print(cnt_y)
print(cnt_x + cnt_y)