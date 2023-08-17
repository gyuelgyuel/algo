import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    line = input()
    stack = []
    for s in line:
        if s == '(' or s == '{':
            stack.append(s)
        elif s == ')':
            if len(stack) == 0:
                stack.append(s)
            elif stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s)
        elif s == '}':
            if len(stack) == 0:
                stack.append(s)
            elif stack[-1] == '{':
                stack.pop()
            else:
                stack.append(s)

    if len(stack) == 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
