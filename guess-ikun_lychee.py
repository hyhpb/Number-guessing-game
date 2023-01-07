import time, os
from random import randint


def pr(text: str, enter: bool = True):
    for i in text:
        print(i, end="")
        time.sleep(0.1)
    if enter:
        print()


pr("请输入猜数字的最小范围：", False)
minn = int(input())
pr("请输入猜数字的最大范围：", False)
maxn = int(input())
finalNum = randint(minn, maxn)

print(finalNum)

n = 0
while True:
    pr("请输入你猜的数字：", False)
    gnum = int(input())
    if gnum > finalNum:
        pr("猜大了")
        n += 1
        time.sleep(2)
        os.system("cls")
    elif gnum < finalNum:
        pr("猜小了")
        n += 1
        time.sleep(2)
        os.system("cls")
    else:
        if not n:
            pr("......")
            time.sleep(3)
            raise Exception("恭喜你，摸着了狗屎...运\n请注意，这不是报错！！！")
        else:
            n += 1
            pr("恭喜你，猜对了")
            pr(f"你猜了{n}次")
        break
