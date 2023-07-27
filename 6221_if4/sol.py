import sys
sys.stdin = open('input.txt',encoding = 'utf-8')

rsp = enumerate(['바위','가위','보'])
m1 = input()
m2 = input()
n1 = -1
n2 = -1

for a,b in rsp:
    if b == m1:
        n1 = a
    if b == m2:
        n2 = a

if n1 == -1 or n2 == -1:
    print('wrong input')

if n1 == n2:
    print('Result : Draw')
elif n1 == 2 and n2 == 0:
    print('Result : Man1 Win!')
elif n1 == 0 and n2 == 2:
    print('Result : Man2 Win!')
elif n1 < n2:
    print('Result : Man1 Win!')
elif n1 > n2:
    print('Result : Man2 Win!')
else:
    print('error')