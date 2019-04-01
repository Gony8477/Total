import sys

def turnleft(d):
    if d == 3:
        return 0
    return d + 1

def clean(now_r, now_c, d, turncount):
    # 1. 현재 위치를 청소한다.
    Map[now_r][now_c] = 2
    # 2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
    while turncount != 4:
        d = turnleft(d)
        turncount += 1
        next_r = now_r + dx[d]
        next_c = now_c + dy[d]
        # 2.1 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
        if Map[next_r][next_c] == 0:
            turncount = 0
            clean(next_r, next_c, d, turncount)
            break





N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline())
Map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]