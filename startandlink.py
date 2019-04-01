import sys

N = int(sys.stdin.readline())
ability = [list(map(int, input().split())) for _ in range(N)]
check = [False] * N
answer = 1e9

def dfs(num, index):
    global answer

    # 확인하는 인덱스 범위
    if index == N:
        return
    # 인덱스가 범위안에 있으면 팀나누는 인원 수 확인
    if num == N//2:
        ## 인원수가 반반 나뉘었으면 각 팀의 능력치 확인
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if check[i] and check[j]:
                    start += ability[i][j]
                if not check[i] and not check[j]:
                    link += ability[i][j]
        answer = min(answer, abs(start-link))
        return

    # 선수 확인 & 다음 선수 확인
    check[index] = True
    dfs(num+1, index+1)
    # 다시 되돌려 놓고 진행(경우의 수 조합)
    check[index] = False
    dfs(num, index+1)
dfs(0, 0)
print(answer)