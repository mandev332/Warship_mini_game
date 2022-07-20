import os as o
from random import randint as r

arr1 = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

arr2 = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]


def show(lis):
    o.system('clear')
    c = 1
    for i in lis:
        for a in range(len(i)):
            print('\033[94m+----', end='')
        print('+')
        for j in i:
            if j == ' ':
                print(f'| \033[93m{c:2d} \033[94m', end='')
            elif j == '0':
                print(f'|    ', end='')
            elif j == '*':
                print('| \033[91m** \033[94m', end='')
            else:
                print(f'| \033[92m{j} \033[94m', end='')
            c += 1

        print(f'|')
    for a in range(len(i)):
        print('+----', end='')
    print('+')


def show2(lis, lis2):
    o.system('clear')
    c = 1
    for i in lis:
        for a in range(len(i)):
            print('\033[94m+----', end='')
        print('+')
        for j in i:
            if j == '*':
                print('| 💥 \033[94m', end='')
            elif j == '0':
                print(f'|    ', end='')
            else:
                print(f'| \033[93m{c:2d} \033[94m', end='')
            c += 1

        print(f'|')
    for a in range(len(i)):
        print('+----', end='')
    print('+')
    print()
    l = 1
    for i in lis2:
        for a in range(len(i)):
            print('\033[94m+----', end='')
        print('+')
        for j in i:
            if j == '*':
                print('| 💥 \033[94m', end='')
            elif j == '0':
                print(f'|    ', end='')
            else:
                print(f'| \033[93m{l:2d} \033[94m', end='')
            l += 1

        print(f'|')
    for a in range(len(i)):
        print('+----', end='')
    print('+')


def insert(lis, P, H):
    q = (P-1) % len(lis[0])
    u = (P-1)//len(lis[0])
    if H == "A":
        if not lis[u+3]:
            return 0
        for i in range(4):
            lis[u+i][q] = '🛳 '
    elif H == "B":
        if not lis[u][q+3]:
            return 0
        for i in range(4):
            lis[u][q+i] = '⛴ '
    elif H == "C":
        if not lis[u+2]:
            return 0
        for i in range(3):
            lis[u+i][q] = '🚢'
    elif H == "D":
        if not lis[u][q+2]:
            return 0
        for i in range(3):
            lis[u][q+i] = '🚤'
    elif H == "E":
        if not lis[u+1]:
            return 0
        for i in range(2):
            lis[u+i][q] = '🛥 '
    elif H == "F":
        if not lis[u][q+1]:
            return 0
        for i in range(2):
            lis[u][q+i] = '⛵️'
    elif H == "I":
        lis[u][q] = '🛶'
    elif H == "G":
        lis[u][q] = '🛶'
    show(lis)


def check_com(lis):
    count = 0
    for i in lis:
        for j in i:
            if j != " ":
                count += 1
    if count == 20:
        return 0
    for i in lis:
        for j in range(len(i)):
            if i[j] != " ":
                i[j] = ' '
    return 1


def game_com(lis):
    kemalar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I']
    s = 0
    while(s != 8):
        try:
            p = r(1, 90)
            if p > 90 or p < 1:
                continue
            insert(lis, p, kemalar[s])
            s += 1
        except:
            continue
    if check_com(lis):
        game_com(lis)


def game(lis, player):
    kemalar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I']
    show(lis)
    s = 0
    while(s != 8):
        print(player, ':')
        try:
            p = int(input(">>> "))
            if p > 90 or p < 1:
                continue
            insert(lis, p, kemalar[s])
            s += 1
        except:
            print("xatolik tekshiring! va qayta yozing!")
            continue


def shot(lis, p):
    q = (p-1) % len(lis[0])
    u = (p-1)//len(lis[0])
    if lis[u][q] != " " and lis[u][q] != "0":
        lis[u][q] = "*"
        return 1
    lis[u][q] = "0"
    return 0


def check(lis):
    count = 0
    for i in lis:
        for j in i:
            if j == "*":
                count += 1
    if count == 20:
        return 1
    return 0
