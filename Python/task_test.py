# 1
txt = open("etl_log.txt", mode="r", encoding="utf-8")
for line in txt:

# 3
[10, a]
[123]
[10, a]

# 4
import sys
v = sys.argv

# 6
l = [i for i in range(1, 101) if i % 2 == 0]

# 7
add = lambda x,y : x+y

# 8
[6,6,6,6]

# 10
import time
def timer(func):
    def inner():
        start = time.time()
        res = func()
        end = time.time()
        message = f"耗时: {end-start}"
        print(message)
        return res
    return inner




