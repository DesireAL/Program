# 输入框模块 绘制输入框与输入框内的字符串
import pygame
import random

pygame.mixer.init()

key_down1 = pygame.mixer.Sound("../sounds/键盘打字1.wav")
key_down1.set_volume(0.2)
key_down2 = pygame.mixer.Sound("../sounds/键盘打字2.wav")
key_down2.set_volume(0.2)
key_down3 = pygame.mixer.Sound("../sounds/键盘打字3.wav")
key_down3.set_volume(0.2)
key_down4 = pygame.mixer.Sound("../sounds/键盘打字4.wav")
key_down4.set_volume(0.2)
key_down5 = pygame.mixer.Sound("../sounds/键盘打字5.wav")
key_down5.set_volume(0.2)

mouse_click = pygame.mixer.Sound("../sounds/鼠标点击1.wav")
mouse_click.set_volume(0.2)

class InputBox:
    def __init__(self):

        self.boxBody = pygame.Rect(125,255,550,50)   # 设置输入框位置与大小
        self.color_inactive = "grey"  # 未被选中的颜色
        self.color_active = "white"  # 被选中的颜色
        self.color = self.color_inactive  # 当前颜色，初始为未激活颜色
        self.active = False
        self.text = '' # 输入的内容
        self.font = pygame.font.Font('C:/Windows/Fonts/simhei.ttf', 32)


    def dealevent(self, event, screen):

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.boxBody.collidepoint(event.pos):  # 若按下鼠标且位置在文本框
                mouse_click.play()
                self.active = not self.active
            else:
                self.active = False

            if self.active:
                self.color = self.color_active
            else:
                self.color = self.color_inactive

        if self.active == True:
            pygame.draw.rect(screen, 'grey', (128,252,550,50), 4)
            pygame.draw.rect(screen, 'grey', (127,253,550,50), 4)
            pygame.draw.rect(screen, 'grey', (126,254,550,50), 4)
            pygame.draw.rect(screen, 'grey', (125,255,550,50), 4)
        else:
            pygame.draw.rect(screen, (65,65,65), (128,252,550,50), 4)
            pygame.draw.rect(screen, (65,65,65), (127,253,550,50), 4)
            pygame.draw.rect(screen, (65,65,65), (126,254,550,50), 4)
            pygame.draw.rect(screen, (65,65,65), (125,255,550,50), 4)

        if event.type == pygame.KEYDOWN:  # 键盘输入响应
            if self.active:
                if event.key == pygame.K_RETURN:
                    start = self.text
                    self.text = ""  # 每次回车后输入框清空
                    self.active = False
                    if start == 'start':
                        print("用户输入了start")
                        self.active = False
                        return 'start'
                    else:
                        #print(start)    # 终端显示返回值
                        return start
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, event, screen):
        if event.type == pygame.KEYDOWN:
            if self.active == True:
                i = random.randint(1,5)
                if i == 1:
                    key_down1.play()
                if i == 2:
                    key_down2.play()
                if i == 3:
                    key_down3.play()
                if i == 4:
                    key_down4.play()
                if i == 5:
                    key_down5.play()
                    print(f"输入")

        txtSurface = self.font.render(self.text, True, "black")  # 文字转换为图片
        pygame.draw.rect(screen, self.color, self.boxBody, 0)   # 绘制输入框
        screen.blit(txtSurface, (self.boxBody.x+5, self.boxBody.y+5))   # 绘制文字
