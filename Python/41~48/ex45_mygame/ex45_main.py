#用Python写《“笨办法”学Python3》
import sys
#import re
import print as p
from time import sleep


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

        p.Ip(0, 1, time, time3), input(), print("\n")

        while current_level != last_level:
            next_level_num = current_level.enter()  #开始运行关卡并获取返回值
            current_level = self.level_num.next_level(next_level_num)   #调用字典
            #print(f">>>>>>>>>>>>>>>{current_level}")

        current_level.enter()   #运行最后一关

        #选关设置

class Ex1(Levels):

    def enter(self):
        p.printline(11, 15, time, time3)
        while True:
            p.Ip(6, 7, time, time3)
            a = input()
            print("\n")
            p.Ip(32, 33, time, time3)
            print(a), print("\n")
            sleep(time)
            c = 'print("' ; d = '")'  #bug:若玩家输入print("")后再输入内容  应该也会正常打印
            e = "print('" ; f = "')"  #太麻烦了不想修
            if (c in a and d in a):
                a = a.rstrip('")')
                a = a.lstrip('print("')
                p.Ip(34, 35, time, time3)
                print(a), print("\n")
                sleep(time)
                p.Ex(80, 81, time, time3)
                p.Ip(8, 9, time, time3)
                b = input()
                print("\n")
                if b == "2":
                    continue
                elif b == "1":
                    break
                else:
                    sleep(time)
                    p.Ex(7, 9)  #没有彩蛋声明
                    continue
            elif e in a and f in a:
                a = a.rstrip("')")
                a = a.lstrip("print('")
                sleep(time)
                p.Ex(34, 35, time, time3)
                print(a), print("\n")
                sleep(time)
                p.Ex(1, 6, time, time3) #单引号提示
                p.Ip(10, 11, time, time3), input(), print("\n")
                break
            else:
                sleep(time)
                p.Ex(10, 13, time, time3)   #指令错误
        return 'ex2'


class Ex2(Levels):

    def enter(self):
        p.printline(15, 21, time, time3)
        while True:
            stop = 1
            p.Ip(12, 13, time, time3)
            a = input()
            print("\n")
            sleep(time)
            p.Ip(32, 33, time, time3)
            print(a), print("\n")
            sleep(time)
            if len(a) == 0:
                p.Ex(82, 83, time, time3)
                continue
            elif a[0] != "#":
                p.Ex(15, 19, time, time3)  #没在开头输入#
                continue
            else:
                a = a[1:]
                p.Ip(34, 35, time, time3)
                print(a), print("\n")
                sleep(time)
                p.Ip(14, 15, time, time3)
                b = input()
                print("\n")
                if b == "1":
                    break
                else:
                    continue
        return 'ex3'


class Ex3(Levels):

    def enter(self):
        p.printline(21, 37, time, time3)
        while True:
            stop = 2
            p.Ip(16, 17, time, time3)
            formula = input()
            print("\n")
            sleep(time)
            p.Ip(36, 37, time, time3)
            print(formula), print("\n")  #bug：若输入类似5+的会报错
            formula = formula.replace(" ", "")
            sleep(time)
            for i in formula:
                if i not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', '%']:
                    p.Ex(38, 40, time, time3)
                    stop = 3
                    break
                elif '+' == formula or '-' == formula or '*' == formula or '/' == formula or '%' == formula:
                    stop = 1
                    break
                elif '+' not in formula and '-' not in formula and '*' not in formula and '/' not in formula and '%' not in formula: #True or False = True 会运行此elif 应该用and
                    stop = 4
                    break
                elif formula[-1] in ('+', '-', '*', '*', '%'):
                    stop = 5
                    break
                else:
                    stop = 0
                    continue
            if stop == 1 or stop == 2:
                p.Ex(41, 43, time, time3)
                continue
            elif stop == 3:
                continue
            elif stop == 4:
                p.Ex(44, 46, time, time3)
                continue
            elif stop == 5:
                p.Ex(47, 49, time, time3)
            else:
                p.Ip(38, 39, time, time3)
                print(eval(formula)), print("\n")
                sleep(time)
                p.Ex(50, 51, time, time3)
                p.Ip(18, 19, time, time3)
                a = input()
                print("\n")
                if a == "1":
                    break
                else:
                    continue
        return 'ex4'





class Ex4(Levels):

    def enter(self):
        p.printline(37, 42, time, time3)
        while True:
            p.Ip(20, 21, time, time3)
            x = input()
            print("\n")
            sleep(time)
            x = x.replace(" ", "")

            z = []
            for i in x:
                if i != "=":
                    z.append(i)
                else:
                    break
            z = "".join(z)
            x = x.lstrip(z)
            x = x.lstrip("=")
            x = x.lstrip("'\"")
            x = x.rstrip("'\"")
            k = x.replace(".", "")

            if k.isdigit():
                p.Ex(84, 85, time, time3)
                sleep(time)
            elif x.isalnum():
                p.Ex(23, 27, time, time3)   #字符串加引号提示
            else:
                p.Ex(86, 87, time, time3)
                sleep(time)
                continue

            p.Ip(22, 23, time, time3)
            y = input()
            y = y.replace(" ", "")
            print("\n")
            sleep(time)
            a = 'print(' ; b = ')'
            c = 'print("' ; d = '")'
            e = "print('" ; f = "')"

            if c in y and d in y:
                y = y.lstrip(c)
                y = y.rstrip(d)
                print(f"{y}\n")
                sleep(time)
                p.Ex(28, 30, time, time3)   #多输双引号
                continue
            elif e in y and f in y:
                y = y.lstrip(e)
                y = y.rstrip(f)
                print(f"{y}\n")
                sleep(time)
                p.Ex(31, 33, time, time3)  #多数单引号
                continue
            elif (a in y) and (b in y):
                y = y.lstrip(a)
                y = y.rstrip(b)
                if z == y:
                    print(x)
                    print("\n")
                    p.Ex(34, 36, time, time3)   #输出结果
                    p.Ip(24, 25, time, time3)
                    q = input()
                    print("\n")
                    if q == "1":
                        break
                    else:
                        continue
                else:
                    print(y),print("\n")
                    sleep(time)
                    p.Ex(88, 89, time, time3)
                    continue
            else:
                p.Ex(90, 91, time, time3)
                sleep(time)
                continue
        return 'ex5'


class Ex5(Levels):

    def enter(self):
        p.printline(42, 49, time, time3)
        while True:
            p.Ip(26, 27, time, time3)
            command = input()
            print("\n")
            sleep(time)
            command = command.replace(" ", "")

            if len(command) == 0:
                p.Ex(53, 54, time, time3)
                continue
            elif command[0].isdigit():
                p.Ex(55, 56, time, time3)
            elif "=" in command:
                subscript = command.index("=")  #判断=位置
            else:
                p.Ex(57, 58, time, time3)
                continue

            variable = command[:subscript] #切片获取变量名
            string = command[subscript + 1:] #切片获取字符串

            if (string[0] == "'" or string[0] == '"') and string[0] == string[-1]:
                string = string[1:-1]
            elif string.isdigit():
                pass
            elif (string[0] == "'" or string[0] == '"') or (string[-1] == "'" or string[-1] == '"'):
                p.Ex(59, 60, time, time3)
                continue
            else:
                p.Ex(61, 62, time, time3)
                continue

            p.Ex(63, 66, time, time3)
            p.Ip(28, 29, time, time3)
            answer = input()
            print("\n")
            if (answer[:8] == "print(f'" and answer[-2:] == "')") or (answer[:8] == 'print(f"' and answer[-2:] == '")'):
                answer = answer[8:-2]
                if "{" in answer and "}" in answer:
                    string1 = answer.index("{")
                    string2 = answer.index("}")
                    if answer[string1+1:string2] == variable:
                        print(f"{answer[:string1]}{string}{answer[string2+1:]}\n")
                        sleep(time)
                        p.Ex(67, 68, time, time3)
                        p.Ip(30, 31, time, time3)
                        q = input()
                        print("\n")
                    else:
                        p.Ex(69, 70, time, time3)
                        continue
                else:
                    p.Ex(71, 72, time, time3)
                    continue
                if q == "1":
                    break
                else:
                    continue
            else:
                p.Ex(73, 74, time, time3)
                continue
        p.Ex(75, 76, time, time3)


class Num(object):

    All_levels = {
            'ex1' : Ex1(),
            'ex2' : Ex2(),
            'ex3' : Ex3(),
            'ex4' : Ex4(),
            'ex5' : Ex5(),
                 }

    def __init__(self, first_level):
        self.first_level = first_level

    def opening_level(self):
        return self.next_level(self.first_level)    #ex1从next_level中获得Ex1()并返回

    def next_level(self, level_name):
        val = Num.All_levels.get(level_name)    #获取字典中的关卡数
        return val  #返回关卡数

sleep(1.5)    #正常为1.5
p.Ex(92, 93, 1.5, 0.1)
p.Ex(94, 95, 1.5, 0.1)
while True:
    p.Ip(2, 3, 1.0, 0.1)
    time = input()
    print("\n")
    p.Ip(4, 5, 1.0, 0.1)
    time3 = input()
    print("\n")
    time2 = time.replace(".", "")
    time4 = time3.replace(".", "")
    if time2.isdigit() and time4.isdigit():
        time = float(time)
        time3 = float(time3)
        break
    else:
        p.Ex(78, 79, 1.0, 0.1)
        continue

sleep(time)
p.printline(0, 11, time, time3)
#start_level = Num('ex1')   #只运行一次的第一关
#state_game = Engine(start_level)
start_game = Engine(Num('ex1')) #将Ex1()返回到 Engine
start_game.play()
