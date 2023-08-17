import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    V, E = map(int,input().split())
    nodes = []
    for _ in range(V):
        nodes.append([])
    for _ in range(E):
        n, m = map(int,input().split())
        nodes[n-1].append(m)
        nodes[m-1].append(n)
    S, G = map(int,input().split())

    check_list = [0]*V
    now = S
    queue = []
    queue.append(S)
    while (len(queue)):
        now = queue.pop(0)
        if now==G:
            break
        for i in nodes[now-1]:
            if check_list[i-1]==0:
                queue.append(i)
                check_list[i-1] = check_list[now-1]+1
            else:
                if check_list[i-1] > check_list[now-1]+1:
                    check_list[i-1] = check_list[now-1]
    print(f'#{tc} {check_list[G-1]}')