from time import sleep
import pygame
from draw import InputBox

text_level = open("../docs/level_introduce.txt", encoding='utf-8')
text_ex = open("../docs/ex_dialogue.txt", encoding='utf-8')
text_ip = open("../docs/InPut.txt", encoding='utf-8')
lines_level = text_level.readlines()
lines_ex = text_ex.readlines()
lines_ip = text_ip.read().splitlines()

pygame.init()
f = pygame.font.Font('C:/Windows/Fonts/simhei.ttf',30)
clock = pygame.time.Clock()
inputbox = InputBox()

#def printline(i, j, time, time3):
#    a = lines_level[i: j]
#    for line in a:
#        for x in line:
#            print(x, end = "", flush = True)
#            sleep(time3)
#        print("\n")
#        sleep(time)

#def Ex(i, j, time, time3):
#    b = lines_ex[i: j]
#    for line in b:
#        for y in line:
#            print(y, end = "", flush = True)
#            sleep(time3)
#        print("\n")
#        sleep(time)

#def Ip(i, j, time, time3):
#    b = lines_ip[i: j]
#    for line in b:
#        for y in line:
#            print(y, end = "", flush = True)
#            sleep(time3)
#        print(" ",end = "")

def Ex(i, j, event, screen, time, time3):   # 也许可以优化简练代码 目前暂不考虑
    b = lines_ex[i: j]
    b = [line.strip('\n') for line in b]    # 将列表b中的元素去掉\n生成新列表赋予b
    #print(f">>>b = {b}") # 调试用 显示游戏文本列表
    for i in b:
        string = '' ; string2 = '' ; z = 0 ; row = 1 ; rows = 0
        for j in range(len(i)):
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.fill((89,89,89))
            if row >= 3: # 打印第三行
                rows = 1
                text3 = f.render(string3,True,('white'))
                inputbox.dealevent(event, screen)
                inputbox.draw(event, screen)
                screen.blit(text3, (130,55))
                pygame.display.flip()
            if row >= 2:    # 打印第二行
                text = f.render(string2,True,('white'))
                inputbox.dealevent(event, screen)
                inputbox.draw(event, screen)
                screen.blit(text, (130,125))
                pygame.display.flip()
            if z < 18:  # 打印第一行
                string += i[j]
                text1 = f.render(string,True,('white'))
                inputbox.dealevent(event, screen)
                inputbox.draw(event, screen)
                screen.blit(text1, (130,195))
                z += 1
                pygame.display.flip()
                sleep(time) # 字间隔时间
            else:   # 一行字数超过18个字之后换行
                if rows == 0:   # 当开始打印第三行后 string3
                    string3 = string2
                row += 1 ; string2 = string ; string = i[j] ; z = 1
                text2 = f.render(string,True,('white'))
                inputbox.dealevent(event, screen)
                inputbox.draw(event, screen)
                screen.blit(text2, (130,195))
                pygame.display.flip()

        sleep(time3)    # 句间隔时间


def Ip(i, j, event, screen, time, time3):   # 也许可以优化简练代码 目前暂不考虑
    b = lines_ip[i: j]
    b = [line.strip('\n') for line in b]    # 将列表b中的元素去掉\n生成新列表赋予b
    #print(f">>>b = {b}") # 调试用 显示游戏文本列表
    for i in b:
        string = '' ; string2 = '' ; z = 0 ; row = 1 ; rows = 0
        for j in range(len(i)):
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.fill((89,89,89))
            if row >= 3: # 打印第三行
                rows = 1
                text3 = f.render(string3,True,('white'))
                inputbox.dealevent(event, screen)
                inputbox.draw(event, screen)
                screen.blit(text3, (130,55))
                pygame.display.flip()
            if row >= 2:    # 打印第二行
                text = f.render(string2,True,('white'))
                inputbox.dealevent(event, screen)
                inputbox.draw(event, screen)
                screen.blit(text, (130,125))
                pygame.display.flip()
            if z < 18:  # 打印第一行
                string += i[j]
                text1 = f.render(string,True,('white'))
                inputbox.dealevent(event, screen)
                inputbox.draw(event, screen)
                screen.blit(text1, (130,195))
                z += 1
                pygame.display.flip()
                sleep(time) # 字间隔时间
            else:   # 一行字数超过18个字之后换行
                if rows == 0:   # 当开始打印第三行后 string3
                    string3 = string2
                row += 1 ; string2 = string ; string = i[j] ; z = 1
                text2 = f.render(string,True,('white'))
                inputbox.dealevent(event, screen)
                inputbox.draw(event, screen)
                screen.blit(text2, (130,195))
                pygame.display.flip()

        sleep(time3)    # 句间隔时间


def Pl(i, j, event, screen, time, time3):   # 也许可以优化简练代码 目前暂不考虑
    b = lines_level[i: j]
    b = [line.strip('\n') for line in b]    # 将列表b中的元素去掉\n生成新列表赋予b
    #print(f">>>b = {b}") # 调试用 显示游戏文本列表
    for i in b:
        string = '' ; string2 = '' ; z = 0 ; row = 1 ; rows = 0
        for j in range(len(i)):
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.fill((89,89,89))
            if row >= 3: # 打印第三行
                rows = 1
                text3 = f.render(string3,True,('white'))
                inputbox.dealevent(event, screen)
                inputbox.draw(event, screen)
                screen.blit(text3, (130,55))
                pygame.display.flip()
            if row >= 2:    # 打印第二行
                text = f.render(string2,True,('white'))
                inputbox.dealevent(event, screen)
                inputbox.draw(event, screen)
                screen.blit(text, (130,125))
                pygame.display.flip()
            if z < 18:  # 打印第一行
                string += i[j]
                text1 = f.render(string,True,('white'))
                inputbox.dealevent(event, screen)
                inputbox.draw(event, screen)
                screen.blit(text1, (130,195))
                z += 1
                pygame.display.flip()
                sleep(time) # 字间隔时间
            else:   # 一行字数超过18个字之后换行
                if rows == 0:   # 当开始打印第三行后 string3
                    string3 = string2
                row += 1 ; string2 = string ; string = i[j] ; z = 1
                text2 = f.render(string,True,('white'))
                inputbox.dealevent(event, screen)
                inputbox.draw(event, screen)
                screen.blit(text2, (130,195))
                pygame.display.flip()

        sleep(time3)    # 句间隔时间
