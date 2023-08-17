import sys
sys.stdin=open('input.txt')
T = int(input())

for tc in range(1,T+1):
    K, N, M = list(map(int,input().split()))
    stations = list(map(int,input().split()))
    elec = K
    elec_if = K
    charge_cnt = 0
    for i in range(1,N+1):
        elec -= 1
        elec_if -= 1
        # print(f'station {i}')
        # print(elec, elec_if, charge_cnt)
        if i in stations:
            if elec < 0:
                charge_cnt = 0
                break
            elif elec_if == 0:
                elec_if = K
                charge_cnt += 1
            elif elec_if < 0:
                elec_if = elec
                charge_cnt += 1
            elec = K
        else:
            if elec_if < 0:
                elec_if = elec
                charge_cnt += 1
    print(f'#{tc} {charge_cnt}')
            
