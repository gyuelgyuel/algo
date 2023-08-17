import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int,input().split()))
    word_mat = []
    strings = []
    circular_string = ''

    ## word_mat 작성
    for n in range(N):
        word_mat.append(input())

    ## 가로 string 추출
    for i in range(N):
        for m in range(N-M+1):
            strings.append(word_mat[i][m:M+m])
    
    ## 세로 string 추출
    for j in range(N):
        for start_i in range(N-M+1):
            string = ''
            for m in range(M):
                string = string + word_mat[start_i+m][j]
            strings.append(string)

    ## 회문인지 검사
    for s in strings:
        r_s = s[::-1]
        if s == r_s:
            circular_string = s
    
    print(f'#{tc} {circular_string}')