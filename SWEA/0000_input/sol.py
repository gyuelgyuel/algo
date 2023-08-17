import sys
sys.stdin = open('input.txt')

TC = int(input())

for i in range(TC):
    N=input()
#    print(N)

nums = input().split()
#print(nums)
for n in nums:
    print(n)

element_num = int(input())
matrix0 = []

for i in range(element_num):
    elements = list(map(int,input().split()))
    matrix0.append(elements)

N, M = list(map(int, input().split()))
matrix = []
for i in range(N):
    numbers = list(map(int, input().split()))
    matrix.append(numbers)

for row in range(len(matrix)):
    print(matrix[row])