from time import sleep as slp
from random import randint as r
import os as o
from war_lib import *


def start():
    player1 = input("pl1: ")
#     player1 = 'Jamshid'
    player2 = 'KOM'
    shoot = []

    game(arr1, player1)
    game_com(arr2)
    e = 1
    while(1):
        slp(2)
        if e % 2:
            show2(arr2, arr1)
            print(player1, '🎯:')
            try:
                p = int(input(">>> "))
                if p > 90 or p < 1:
                    continue
                if not (shot(arr2, p)):
                    show2(arr2, arr1)
                    e += 1
            except:
                print("xatolik tekshiring! va qayta yozing!")
                continue

        else:
            show2(arr1, arr2)
            slp(2)
            print(player2, '🎯:')
            try:
                p = r(1, 90)
                if p in shoot:
                    continue
                if not (shot(arr1, p)):
                    show2(arr1, arr2)
                    e += 1
                shoot.append(p)
            except:
                print("xatolik tekshiring! va qayta yozing!")
                continue
        if check(arr1) or check(arr2):
            break


start()
show(arr1, arr2)
