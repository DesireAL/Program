from time import sleep

text_level = open("level_introduce.txt", encoding='utf-8')
text_ex = open("ex_dialogue.txt", encoding='utf-8')
text_ip = open("InPut.txt", encoding='utf-8')
lines_level = text_level.readlines()
lines_ex = text_ex.readlines()
lines_ip = text_ip.read().splitlines()

def printline(i, j, time, time3):
    a = lines_level[i: j]
    for line in a:
        for x in line:
            print(x, end = "", flush = True)
            sleep(time3)
        print("\n")
        sleep(time)

def Ex(i, j, time, time3):
    b = lines_ex[i: j]
    for line in b:
        for y in line:
            print(y, end = "", flush = True)
            sleep(time3)
        print("\n")
        sleep(time)

def Ip(i, j, time, time3):
    b = lines_ip[i: j]
    for line in b:
        for y in line:
            print(y, end = "", flush = True)
            sleep(time3)
        print(" ",end = "")
