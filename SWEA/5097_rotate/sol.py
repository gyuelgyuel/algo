import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    queue = list(map(int,input().split()))
    for _ in range(M):
        queue.append(queue[0])
        del queue[0]
    print(f'#{tc} {queue[0]}')