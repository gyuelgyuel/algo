import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())
stack = [1,3]
for tc in range(1, T+1):
    N = int(input())
    n = int(N/10)
    if n > len(stack):
        for _ in range(n - len(stack)):
            stack.append(stack[-1]+stack[-2]*2)
    print(f'#{tc} {stack[n-1]}')