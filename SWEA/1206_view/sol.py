import sys
sys.stdin=open('input.txt')

for tc in range(1,11):
    b_num = int(input())
    buildings = list(map(int,input().split()))
    view_num = 0
    for i in range(2,b_num-2):
        height_max = max(buildings[i-2:i]+buildings[i+1:i+3])
        if height_max < buildings[i]:
            view_num += buildings[i]-height_max
    print(f'#{tc} {view_num}')