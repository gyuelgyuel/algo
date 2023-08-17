import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    V, E = list(map(int,input().split()))

    nodes = [ [] for _ in range(V+1) ]

    for line in range(E):
        start, end = list(map(int,input().split()))
        nodes[start].append(end)

    S, G = list(map(int,input().split()))

    check_list = [False] * (V+1)
    stack = []
    check_list[S] = True
    result = 0
    stack.append(S)
    
    while len(stack):
        now = stack.pop()
        check_list[now] = True

        for next in nodes[now]:
            if not check_list[next]:
                if G == next:
                    result = 1
                stack.append(next)
    print(result)
