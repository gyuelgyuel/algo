import sys
sys.stdin = open('input.txt')

char_b = input()

if char_b.isupper():
    char_a = char_b.lower()
    print(f'{char_b}(ASCII: {ord(char_b)}) => {char_a}(ASCII: {ord(char_a)})')
elif char_b.islower():
    char_a = char_b.upper()
    print(f'{char_b}(ASCII: {ord(char_b)}) => {char_a}(ASCII: {ord(char_a)})')
else:
    print(char_b)