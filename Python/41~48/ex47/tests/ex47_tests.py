from nose.tools import *
from ex47.game import Room

def test_room():
    gold = Room("GoldRoom", "这里有许多你可以拿的黄金，还有一扇去往北方的门")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "测试房屋在中间")
    north = Room("North", "测试房屋在北方")
    south = Room("South", "测试房屋在南方")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "你可以去西边并进入一个洞")
    west = Room("Trees", "这里有树，你可以去西边")
    down = Room("Dungeon", "下面很黑，你可以上去")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)
