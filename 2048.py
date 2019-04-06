from collections import deque
n = int(input())
Map = [list(map(int, input().split())) for _ in range(n)]
dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
tmp = [[[] for _ in range(3)] for _ in range(3)]
q = deque()
def value(x, y):
    if Map[x][y] != 0:
        q.append(Map[x][y])
        Map[x][y] = 0
def merge(x, y, dx, dy):
    while q:
        tmp = q.popleft()
        if not Map[x][y]:
            Map[x][y] = tmp
        elif Map[x][y] == tmp:
            Map[x][y] = tmp * 2
            x, y = x + dx, y + dy
        else:
            x, y = x + dx, y + dy
            Map[x][y] = tmp
def bfs(cnt):
    global Map, answer
    if cnt == 5:
        for i in range(n):
            answer = max(answer, max(Map[i]))
        return
    tmp_map = [x[:] for x in Map]
    for i in range(4):
        # 위
        if i == 0:
            for x in range(n):
                for y in range(n):
                    # 첫번째 열부터 행을 차례로 올리기(위로올리기 때문에 yx 바꿔서 보낸다)
                    value(y, x)
                # 각 열마다 확인하기(x가 0, 1, 2순으로 간다.)
                # y = 0, y = x인 이유 : 위로 올리기때문에 x가 0인부분으로 내려가면서(dx +1) 차례대로 싸인다.
                merge(0, x, dx[i], dy[i])
        # 아래
        elif i == 1:
            for x in range(n):
                for y in range(n - 1, -1, -1):
                    # 끝 열부터 행을 차례로 내리기(아래로 내리기 때문에 yx 바꿔서 보낸다)
                    value(y, x)
                # 각 열마다 합치기(x가 0, 1, 2순으로 간다.)
                # x = n-1 y = x인 이유 : 내리면 마지막 열에 쌓이기 떄문에 올라가면서(dx -1) 숫자가 적힌다.
                merge(n-1, x, dx[1], dy[i])
        # 왼쪽
        elif i == 2:
            for x in range(n):
                for y in range(n):
                    # 행에서 부터 열 순서대로 왼쪽에서 가져오기(왼쪽으로 보내기 때문에)
                    value(x, y)
                # x = x, y = 0인 이유 : 왼쪽으로 보내기 때문에 첫번째 열부터(dy +1) 쌓인다.
                merge(x, 0, dx[i], dy[i])
        # 오른쪽
        else:
            for x in range(n):
                for y in range(n - 1, -1, -1):
                    # 행의 마지막부터 열 거꾸로 순으로 오른쪽에서 가져오기(FIFO) 처음에 가져온 부분부터 적어나간다.
                    value(x, y)
                # 행순으로 y = n-1인이유 : 마지막 열에 쌓인다.
                merge(x, n - 1, dx[i], dy[i])
        bfs(cnt+1)
        Map = [x[:] for x in tmp_map]
cnt = 0
answer = 0
bfs(cnt)
print(answer)