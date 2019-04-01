import sys
dragon_num = int(sys.stdin.readline())
dragon = [tuple(map(int, sys.stdin.readline().split())) for _ in range(dragon_num)]
Map = [[0 for _ in range(101)] for _ in range(101)]

for x, y, d, g in dragon:
    # 드래곤 0세대
    direction = []
    Map[y][x] = 1
    if d == 0:
        x += 1
    if d == 1:
        y -= 1
    if d == 2:
        x -= 1
    if d == 3:
        y += 1
    Map[y][x] = 1
    direction.append(d)
    # 방향 관계 누적
    while g != 0:
        # 시작하기 전 앞으로 가야할 방향은 이전 단계에 연결되어 있다. 270도 회전한 방향이다. 0 --> 1, 1 --> 2, 2 --> 3. 3 --> 2
        ## 앞으로 갈방향을 스택에 쌓는다. (used에 쌓았다.)
        used = []
        for i in range(len(direction)):
            if direction[i] == 0:
                used.append(1)
            if direction[i] == 1:
                used.append(2)
            if direction[i] == 2:
                used.append(3)
            if direction[i] == 3:
                used.append(0)
        ### 쌓은 스택을 마지막에서 뽑는다.
        for j in range(len(used)-1, -1, -1):
            if used[j] == 0:
                x += 1
            if used[j] == 1:
                y -= 1
            if used[j] == 2:
                x -= 1
            if used[j] == 3:
                y += 1
            Map[y][x] = 1
            #### 지금 간 방향은 다음 방향에 추가되어야한다.
            direction.append(used[j])
        g -= 1
# 확인할때 인덱스 넘어가면 안된다. 넘어가면 런타임 오류나온다. 주의하자!
answer = 0
for y in range(100):
    for x in range(100):
        if Map[y][x] == 1:
            if Map[y+1][x] == 1 and Map[y][x+1] == 1 and Map[y+1][x+1] == 1:
                answer += 1
print(answer)