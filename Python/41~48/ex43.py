from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("此场景尚未配置")
        print("将其子类化并实现enter()")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #确保打印出最后的场景
        current_scene.enter()


class Death(Scene):

    quips = ["----------死亡提示语----------"]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
              中央走廊提示语，可做出选择
              1.shoot!
              2.dodge!
              3.tell a joke
              """))

        action = input("> ")
        print(action)

        if action == "shoot!":
            print("1提示语")
            return 'death'

        elif action == "dodge!":
            print("2提示语")
            return 'death'

        elif action == "tell a joke":
            print("3提示语")
            return 'laser_weapon_armory'

        else:
            print("请输入选项内容")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print("激光武器库提示语，请输入密码")

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[键盘]> ")
        guesses = 0

        while guess != code and guesses < 9:
            if guess == "help":
                print(code)
            print("耳边出现嗡嗡声")
            guesses += 1
            guess = input("[键盘]> ")

        if guess == code:
            print("密码正确提示语")
            return 'the_bridge'
        else:
            print('密码错误提示语')
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
              主控仓提示语，可作出选择
              1.投出炸弹
              2.慢慢放下炸弹
              """))

        action = input("> ")
        if action == "投出炸弹":
            print("提示语")
            return 'death'
        elif action == "慢慢放下炸弹":
            print("提示语")
            return 'escape_pod'
        else:
            print("请选择1~2或输入选项内容")
            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):
        print("逃生舱提示语，选择逃生舱1~5")

        good_pod = randint(1,5)
        guess = input("> ")

        if str(guess) == "help":
            return 'finished'

        elif int(guess) != good_pod:
            print("坏逃生舱提示语")
            return 'death'

        else:
            print("好逃生舱提示语")
            return 'finished'


class Finished(Scene):

    def enter(self):
        print("你赢了，干得漂亮！")
        return 'finished'


class Map(object):
    scenes = {
              'central_corridor' : CentralCorridor(),
              'laser_weapon_armory' : LaserWeaponArmory(),
              'the_bridge' : TheBridge(),
              'escape_pod' : EscapePod(),
              'death' : Death(),
              'finished' : Finished(),
              }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        value = Map.scenes.get(scene_name)
        return value

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
