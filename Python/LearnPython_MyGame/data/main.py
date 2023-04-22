# 用Python写《“笨办法”学Python3》
import sys
import pygame
import pygame.freetype
from draw import InputBox
from time import sleep
import print as p

# 初始化pygame 创建窗口 设置窗口名
# global screen, time, time3, f
time = 0.1
time3 = 1.5  # time为字间隔,time3为句间隔  ###################0.1   1.5

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("'笨办法'学Python3")
# 创建时钟对象
clock = pygame.time.Clock()
# 设置窗口图片路径
icon = pygame.image.load("mygame.ico")
# 设置窗口的图标
pygame.display.set_icon(icon)
f = pygame.font.Font('C:/Windows/Fonts/simhei.ttf', 30)


class Levels(object):

    def enter(self):
        print("此为父类Levels，没有设置习题")
        exit(1)


class Engine(object):

    def __init__(self, level_num):
        self.level_num = level_num

    def play(self):
        current_level = self.level_num.opening_level()
        last_level = self.level_num.next_level('ex5')

        while current_level != last_level:
            next_level_num = current_level.enter()  # 开始运行关卡并获取返回值
            current_level = self.level_num.next_level(next_level_num)  # 调用字典
            # print(f">>>>>>>>>>>>>>>{current_level}")

        current_level.enter()  # 运行最后一关


class Ex1(Levels):

    def enter(self):
        x = 0
        while True:
            clock.tick(60)
            event = pygame.event.wait()
            pygame.event.set_blocked(pygame.MOUSEMOTION)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            # f = pygame.font.Font('C:/Windows/Fonts/simhei.ttf',30)
            text = inputbox.dealevent(event, screen)
            inputbox.draw(event, screen)

            if x == 0:
                x = 1
                p.Pl(11, 14, event, screen, time, time3)
                continue

            if text == 'pass':  # 调试用
                print('跳过ex1')
                break

            if text is not None and x == 2:
                string = text
                if string == '1':  # 进入Ex2
                    x = 1
                    break
                elif string == '2':  # 再次尝试
                    p.Ip(6, 7, event, screen, time, time3)
                    x = 1
                    continue
                else:  # 无彩蛋，再次尝试
                    p.Ex(7, 9, event, screen, time, time3)
                    p.Ip(6, 7, event, screen, time, time3)
                    x = 1
                    continue

            if text is not None and x == 1:
                string = text
                screen.fill((89, 89, 89))
                text = f.render('你刚刚输入的代码为↓', True, 'white')
                text2 = f.render(string, True, 'white')
                a = 'print("'
                b = '")'  # bug:若玩家输入print("")后再输入内容  应该也会正常打印
                c = "print('"
                d = "')"  # 太麻烦了不想修
                string2 = string.rstrip('")')
                string2 = string2.lstrip('print("')
                string2 = string2.rstrip(")'")
                string2 = string2.lstrip("print('")
                text3 = f.render('运行代码后的结果为↓', True, 'white')
                text4 = f.render(string2, True, 'white')
                if a in string and b in string:
                    # p.Ex(34, 35, event, screen, time, time3)
                    inputbox.dealevent(event, screen)
                    inputbox.draw(event, screen)
                    screen.blit(text, (150, 375))
                    screen.blit(text2, (150, 425))
                    screen.blit(text3, (150, 475))
                    screen.blit(text4, (150, 525))
                    pygame.display.flip()
                    sleep(2)
                    p.Ex(80, 81, event, screen, time, time3)
                    p.Ip(8, 9, event, screen, time, time3)
                    x = 2
                elif c in string and d in string:
                    # p.Ex(34, 35, event, screen, time, time3)
                    p.Ex(1, 6, event, screen, time, time3)  # 单引号提示
                    screen.blit(text, (150, 375))
                    screen.blit(text2, (150, 425))
                    screen.blit(text3, (150, 475))
                    screen.blit(text4, (150, 525))
                    pygame.display.flip()
                    sleep(2)
                    break
                else:
                    p.Ex(10, 13, event, screen, time, time3)
                    p.Ip(6, 7, event, screen, time, time3)
                    screen.blit(text, (150, 375))
                    screen.blit(text2, (150, 425))
                    pygame.display.flip()
                    continue
            pygame.display.flip()
        return 'ex2'


class Ex2(Levels):

    def enter(self):
        x = 0
        while True:
            clock.tick(60)
            event = pygame.event.wait()
            pygame.event.set_blocked(pygame.MOUSEMOTION)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            text = inputbox.dealevent(event, screen)
            inputbox.draw(event, screen)

            if x == 0:
                x = 1
                p.Pl(15, 21, event, screen, time, time3)
                continue

            if text == 'pass':  # 调试用
                print('跳过ex2')
                break

            if text is not None and x == 2:
                string = text
                if string == '1':  # 进入Ex3
                    break
                else:  # 再次尝试
                    p.Ip(12, 13, event, screen, time, time3)
                    x = 1
                    continue

            if text is not None and x == 1:
                screen.fill((89, 89, 89))
                inputbox.dealevent(event, screen)
                inputbox.draw(event, screen)
                if text[0] != '#':  # 没有在开头输入#
                    p.Ex(15, 19, event, screen, time, time3)
                    continue
                else:
                    string = text
                    string2 = text[:]
                    text2 = f.render('你刚刚输入的代码为↓', True, 'white')
                    text = f.render(string, True, 'white')
                    text4 = f.render('屏幕上将显示↓', True, 'white')
                    text3 = f.render(string2, True, 'white')
                    screen.blit(text2, (150, 375))
                    screen.blit(text, (150, 425))
                    screen.blit(text4, (150, 475))
                    screen.blit(text3, (150, 525))
                    pygame.display.flip()
                    sleep(2)
                    p.Ip(14, 15, event, screen, time, time3)
                    x = 2

            pygame.display.flip()
        return 'ex3'


class Ex3(Levels):

    def enter(self):
        x = 0
        while True:
            stop = 2
            clock.tick(60)
            event = pygame.event.wait()
            pygame.event.set_blocked(pygame.MOUSEMOTION)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            text = inputbox.dealevent(event, screen)
            inputbox.draw(event, screen)

            if x == 0:
                p.Pl(21, 37, event, screen, time, time3)
                x = 1
                continue

            if text == 'pass':  # 调试用
                print('跳过ex3')
                break

            if text is not None and x == 2:
                if text == '1':
                    break
                else:
                    p.Ip(16, 17, event, screen, time, time3)
                    x = 1
                    continue

            if text is not None and x == 1:
                formula = text.replace(' ', '')
                for i in formula:
                    if i not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', '%']:
                        p.Ex(38, 40, event, screen, time, time3)
                        stop = 3
                        break
                    elif '+' == formula or '-' == formula or '*' == formula or '/' == formula or '%' == formula:
                        stop = 1
                        break
                    elif '+' not in formula and '-' not in formula and '*' not in formula and '/' not in formula and '%' not in formula:  # True or False = True 会运行此elif 应该用and
                        stop = 4
                        break
                    elif formula[-1] in ('+', '-', '*', '*', '%'):
                        stop = 5
                        break
                    else:
                        stop = 0
                        continue
                if stop == 1 or stop == 2:
                    p.Ex(41, 43, event, screen, time, time3)
                    continue
                elif stop == 3:
                    continue
                elif stop == 4:
                    p.Ex(44, 46, event, screen, time, time3)
                    continue
                elif stop == 5:
                    p.Ex(47, 49, event, screen, time, time3)
                    continue
                else:
                    string = f.render('你输入的公式为↓', True, 'white')
                    string2 = f.render(formula, True, 'white')
                    formula = str(eval(formula))
                    string3 = f.render('答案为↓', True, 'white')
                    string4 = f.render(formula, True, 'white')
                    screen.blit(string, (150, 375))
                    screen.blit(string2, (150, 425))
                    screen.blit(string3, (150, 475))
                    screen.blit(string4, (150, 525))
                    pygame.display.flip()
                    sleep(2)
                    p.Ex(50, 51, event, screen, time, time3)
                    p.Ip(18, 19, event, screen, time, time3)
                    x = 2
                    continue

            pygame.display.flip()
        return 'ex4'


class Ex4(Levels):

    def enter(self):
        x = 0
        while True:
            clock.tick(60)
            event = pygame.event.wait()
            pygame.event.set_blocked(pygame.MOUSEMOTION)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            text = inputbox.dealevent(event, screen)
            inputbox.draw(event, screen)

            if x == 0:
                p.Pl(37, 42, event, screen, time, time3)
                x = 1
                continue

            if text == 'pass':
                print('跳过ex4')
                break

            if text is not None and x == 3:
                if text == '1':
                    break
                else:
                    p.Ip(20, 21, event, screen, time, time3)
                    x = 1
                    continue

            if text is not None and x == 2:  # 第二次输入
                string2 = text
                string2 = string2.replace(" ", "")
                a1 = 'print('
                a2 = ')'
                a3 = 'print("'
                a4 = '")'
                a5 = "print('"
                a6 = "')"
                if a3 in string2 and a4 in string2:  # 多输双引号
                    # string2 = string2.lstrip(a3)
                    # string2 = string2.rstrip(a4)
                    text1 = f.render('你输入的代码为↓', True, 'white')
                    text2 = f.render(string2, True, 'white')
                    screen.blit(text1, (150, 375))
                    screen.blit(text2, (150, 425))
                    pygame.display.flip()
                    sleep(2)
                    p.Ex(28, 30, event, screen, time, time3)
                    x = 1
                    continue
                elif a5 in string2 and a6 in string2:  # 多输单引号
                    # string2 = string2.lstrip(a5)
                    # string2 = string2.rstrip(a6)
                    text1 = f.render('你输入的代码为↓', True, 'white')
                    text2 = f.render(string2, True, 'white')
                    screen.blit(text1, (150, 375))
                    screen.blit(text2, (150, 425))
                    pygame.display.flip()
                    sleep(2)
                    p.Ex(31, 33, event, screen, time, time3)
                    x = 1
                    continue
                elif a1 in string2 and a2 in string2:  # print语句正确
                    string2 = string2.lstrip(a1)
                    string2 = string2.rstrip(a2)
                    if z == string2:  # 变量名与print中的变量名一致
                        text1 = f.render('你输入的代码结果为↓', True, 'white')
                        text2 = f.render(string, True, 'white')
                        screen.blit(text1, (150, 375))
                        screen.blit(text2, (150, 425))
                        pygame.display.flip()
                        sleep(2)
                        p.Ex(34, 36, event, screen, time, time3)  # 输出结果
                        p.Ip(24, 25, event, screen, time, time3)  # 选择继续还是再来一次
                        x = 3
                        continue
                    else:  # 也许变量名输错了,重新开始
                        p.Ex(88, 89, event, screen, time, time3)
                        x = 1
                        continue
                else:  # print语句有误,重新开始
                    p.Ex(90, 91, event, screen, time, time3)
                    x = 1
                    continue

            if text is not None and x == 1:  # 第一次输入
                string = text
                string = string.replace(" ", "")
                z = []
                for i in string:
                    if i != "=":
                        z.append(i)
                    else:
                        break
                z = "".join(z)  # z为变量名
                string = string.lstrip(z)  # 去除第一次输入的变量名
                string = string.lstrip("=")  # 去除第一次输入的=
                string = string.lstrip("'")  # 去除赋值左右的引号
                string = string.lstrip('"')
                string = string.rstrip("'")
                string = string.rstrip('"')
                print(string)
                k = string.replace(".", "")  # 定义一个k来判断是否为纯数字

                if k.isdigit():
                    p.Ex(84, 85, event, screen, time, time3)  # 输入的为纯数字
                elif string.isalnum():
                    p.Ex(23, 27, event, screen, time, time3)  # 输入的为字符串，加引号提示
                else:
                    p.Ex(86, 87, event, screen, time, time3)  # 输入了未知的东西
                    continue

                p.Ip(22, 23, event, screen, time, time3)
                x = 2

            pygame.display.flip()
        return 'ex5'


class Ex5(Levels):

    def enter(self):
        print('进入了ex5')
        x = 0
        while True:
            clock.tick(60)
            event = pygame.event.wait()
            pygame.event.set_blocked(pygame.MOUSEMOTION)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            text = inputbox.dealevent(event, screen)
            inputbox.draw(event, screen)

            if x == 0:
                p.Pl(42, 49, event, screen, time, time3)
                p.Ip(26, 27, event, screen, time, time3)
                x = 1
                continue

            if text == 'pass':
                print('跳过ex5')
                break

            if text is not None and x == 1:
                command = text
                command = command.replace(" ", "")

                if len(command) == 0:
                    p.Ex(53, 54, event, screen, time, time3)  # 输入内容为空，请重试
                    continue
                elif command[0].isdigit():
                    p.Ex(55, 56, event, screen, time, time3)  # 不能使用数字开头的变量名，请重试
                    continue
                elif "=" in command:
                    subscript = command.index("=")  # subscript为=的位置
                else:
                    p.Ex(57, 58, event, screen, time, time3)  # 错误的输入方式，请重试
                    continue

                variable = command[:subscript]  # 切片获取变量名
                string = command[subscript + 1:]  # 切片获取字符串

                if (string[0] == "'" or string[0] == '"') and (string[0] == string[-1]):
                    string = string[1:-1]  # 将字符串的引号去掉
                elif string.isdigit():
                    pass
                elif (string[0] == "'" or string[0] == '"') or (string[-1] == "'" or string[-1] == '"'):
                    p.Ex(59, 60, event, screen, time, time3)  # 引号错误，请重试
                    continue
                else:
                    p.Ex(61, 62, event, screen, time, time3)  # 字符串有误，请重试
                    continue

                p.Ex(63, 66, event, screen, time, time3)
                p.Ip(28, 29, event, screen, time, time3)
                x = 2
                continue

            if text is not None and x == 2:
                answer = text
                if (answer[:8] == "print(f'" and answer[-2:] == "')") or (
                        answer[:8] == 'print(f"' and answer[-2:] == '")'):
                    answer = answer[8:-2]
                    if "{" in answer and "}" in answer:
                        string1 = answer.index("{")  # 判断print语句中的{变量名}位置
                        string2 = answer.index("}")
                        if answer[string1 + 1:string2] == variable:
                            text0 = answer[:string1] + string + answer[string2 + 1:]
                            text1 = f.render('你输入代码的结果为↓', True, 'white')
                            text2 = f.render(text0, True, 'white')
                            screen.blit(text1, (150, 375))
                            screen.blit(text2, (150, 425))
                            pygame.display.flip()
                            sleep(2)
                            p.Ex(67, 68, event, screen, time, time3)
                            p.Ip(30, 31, event, screen, time, time3)
                            x = 3
                            continue
                        else:
                            p.Ex(69, 70, event, screen, time, time3)  # 两次变量名不同，重试
                            continue
                    else:
                        p.Ex(71, 72, event, screen, time, time3)  # 没有输入{变量名}，重试
                        continue
                else:
                    p.Ex(73, 74, event, screen, time, time3)  # 没检测到完整语句，重试
                    continue

            if text is not None and x == 3:
                if text == '1':
                    p.Ex(75, 76, event, screen, time, time3)
                    pygame.display.flip()
                    sleep(2)
                    pygame.quit()
                    sys.quit()
                else:
                    x = 1
                    p.Ip(26, 27, event, screen, time, time3)
                    continue

            pygame.display.flip()


class Num(object):  # 关卡指示模块

    All_levels = {
        'ex1': Ex1(),
        'ex2': Ex2(),
        'ex3': Ex3(),
        'ex4': Ex4(),
        'ex5': Ex5(),
    }

    def __init__(self, first_level):
        self.first_level = first_level

    def opening_level(self):
        return self.next_level(self.first_level)  # ex1从next_level中获得Ex1()并返回

    def next_level(self, level_name):
        val = Num.All_levels.get(level_name)  # 获取字典中的关卡数
        return val  # 返回关卡数


def game():  # 游戏函数
    global time, time3  # time1为字间隔时间0.1 time3为句间隔时间1.5
    while True:
        clock.tick(60)
        event = pygame.event.wait()
        pygame.event.set_blocked(pygame.MOUSEMOTION)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        text = inputbox.dealevent(event, screen)
        inputbox.draw(event, screen)

        if text == 'set time1':
            p.Ip(4, 5, event, screen, time, time3)
            while True:
                clock.tick(60)
                event = pygame.event.wait()
                pygame.event.set_blocked(pygame.MOUSEMOTION)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                times = inputbox.dealevent(event, screen)
                inputbox.draw(event, screen)
                if times is not None:
                    time2 = times.replace('.', '')  # 去除字符串中的. 方便后续的isdigit语句做处理
                    if time2.isdigit():
                        time = float(times)
                        print("用户设置字间隔为{}".format(time))
                        p.Ip(40, 43, event, screen, time, time3)
                        break
                    else:
                        p.Ex(78, 79, event, screen, time, time3)
                        p.Ip(4, 5, event, screen, time, time3)
                pygame.display.flip()

        if text == 'set time2':
            p.Ip(2, 3, event, screen, time, time3)
            while True:
                clock.tick(60)
                event = pygame.event.wait()
                pygame.event.set_blocked(pygame.MOUSEMOTION)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                times = inputbox.dealevent(event, screen)
                inputbox.draw(event, screen)
                if times is not None:
                    time4 = times.replace('.', '')  # 去除字符串中的. 方便后续的isdigit语句做处理
                    if time4.isdigit():
                        time3 = float(times)
                        print("用户设置句间隔为{}".format(time3))
                        p.Ip(40, 43, event, screen, time, time3)
                        break
                    else:
                        p.Ex(78, 79, event, screen, time, time3)
                        p.Ip(4, 5, event, screen, time, time3)
                pygame.display.flip()

        if text == 'start':
            print('游戏正式开始')
            #            p.Pl(0, 11, event, screen, time, time3)
            start_game = Engine(Num('ex1'))  # 将Ex1()返回到 Engine
            start_game.play()
        elif text is not None and text in ('ex1', 'ex2', 'ex3', 'ex4', 'ex5'):  # 调试用 可跳关 输入其他东西会报错
            start_game = Engine(Num(text))
            start_game.play()

        pygame.display.flip()


if __name__ == "__main__":
    inputbox = InputBox()
    while True:  # 游戏开始前主体循环
        clock.tick(60)  # 限制帧数
        screen.fill((89, 89, 89))  # 必须将底色放入循环中，否则在text改变后无法覆盖删去的文字
        f1 = pygame.freetype.Font('C:/Windows/Fonts/simhei.ttf')  # 引入字体类型
        title = f1.render_to(screen, (116, 100), "<'笨办法'学Python3>", fgcolor="white", size=60)  # 打印标题
        tips = f1.render_to(screen, (57, 400), "输入start并回车开始游戏", fgcolor="white", size=60)
        tips2 = f1.render_to(screen, (360, 565), "没找到合适的bgm，所以没有音乐", fgcolor='white', size=30)
        # f = pygame.font.Font('C:/Windows/Fonts/simhei.ttf',30)
        # 生成文本信息，第一个参数文本内容；第二个参数，字体是否平滑；
        # 第三个参数，RGB模式的字体颜色；第四个参数，RGB模式字体背景颜色；
        # text = f.render("<'笨办法'学Python3>",True,(255,255,255))
        # textRect =text.get_rect()   # 获得显示对象的rect区域坐标
        # textRect.center = (400,125) # 设置显示对象居中
        # screen.blit(text,textRect)  # 将准备好的文本信息，绘制到主屏幕 Screen 上。

        pygame.event.set_blocked(pygame.MOUSEMOTION)
        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        # p.Pl(0, 50, event, screen, time, time3)    # 调试自建print模块用
        text = inputbox.dealevent(event, screen)
        inputbox.draw(event, screen)

        if text != "start":  # 若未输入start 则没有事情发生
            pass
            # inputbox.draw(event, screen)
            # pygame.display.flip()
        elif text == "QUIT":  # 若输入QUIT 则退出程序
            pygame.quit()
            sys.exit()
        else:  # 若输入start 则进入下一个循环
            print("游戏开始")
            screen.fill((89, 89, 89))  # 填充一次画面将两句提示语覆盖掉
            sleep(0.5)
            p.Ex(92, 95, event, screen, time, time3)  # 调用自建库函数 打印游戏文本
            p.Ip(40, 43, event, screen, time, time3)
            game()

        pygame.display.flip()
