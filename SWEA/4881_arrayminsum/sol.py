import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

def find_min_sum(mat,elem_list,p_sum,min_sum): # input : number matrix, list of index unused, prior sum
    n = len(mat)                       # output : total sum
    m = len(elem_list)

    if m == 0:              # return prior sum if nothing to sum more
        return p_sum
    else:
        for i in elem_list:
            p0_sum = p_sum + mat[n-m][i]    # prior sum + i th element
            if p0_sum < min_sum:            # only recursive when prior sum is less than min sum
                idx = elem_list.index(i)
                #                           elem_list except i
                temp_sum = find_min_sum(mat,elem_list[:idx]+elem_list[idx+1:],p0_sum,min_sum)
                if temp_sum < min_sum:      # compare to configure minimum
                    min_sum = temp_sum
        return min_sum

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    ## make num_matrix
    num_matrix = []
    for _ in range(N):
        num_matrix.append(list(map(int,input().split())))

    ## find minimum sum
    print(f'#{tc} {find_min_sum(num_matrix,list(range(N)),0,99999)}')