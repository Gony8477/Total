import sys

##DFS로 접근
def find(num):
    global min_cnt, channel

    for button in remote:
        tmp_num = num + str(button)
        min_cnt = min(min_cnt, abs(channel - int(tmp_num))+len(tmp_num))

        if len(tmp_num) < 6:
            find(tmp_num)

channel = int(input())
n = int(input())
remote = {i for i in range(10)}
remote -= set(map(int, input().split())) if n else set()
min_cnt = abs(100 - channel)
find('') if n < 10 else ''

print(min_cnt)