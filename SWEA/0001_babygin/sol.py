import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    numbers = input()                   #
    cnt = 0                             # count run or triplet
    cnt_same = 0                        # count same element (triplet)
    cnt_inc = 0                         # count increase element (run)
    e_p = -2                            # previous element
    list1 = []                          
    for w in numbers:                   # change string to list[int]
        list1.append(int(w))

    list1.sort()                        # sort increase order

    for e in list1:
        if e == e_p:                    # if element and previous element is same
            cnt_same+=1                 # cnt_same + 1 and reset cnt_inc
            cnt_inc=0
        elif e == e_p+1:                # if element is 1 larger than previous element
            cnt_inc+=1                  # cnt_inc + 1 and reset cnt_same
            cnt_same=0
        else:
            cnt_inc=0                   # else (not run or triplet) reset cnt_same,cnt_inc
            cnt_same=0
        if cnt_same==2 or cnt_inc==2:   # if run or triplet, cnt + 1 and reset previous element
            cnt+=1
            e_p=-2
        else:                           # if not run or triplet, update previous element
            e_p = e

    if cnt==2:                          # if cnt = 2, it means baby gin
        print(f'#{tc} True')
    else:
        print(f'#{tc} False')

