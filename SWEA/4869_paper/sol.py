import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

def fact(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

for tc in range(1, T+1):
    N = int(input())
    n = int(N/10)
    case_num = 0
    for j in range(int(n/2)+1): # j는 가로길이 20의 종이 개수
        i = n - 2*j # i는 가로길이 10의 종이 개수
        case_num += int(fact(i+j)/(fact(i)*fact(j))*(2**j))
    print(f'#{tc} {case_num}')