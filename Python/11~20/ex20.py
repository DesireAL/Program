from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline(), end="")
#当前文件为argv中输入的文件名
current_file = open(input_file, encoding = 'utf-8')

print("First let's print the whole file:\n")
#打印全部文件内容
print_all(current_file)

print("Now Let's rewind, kind of like a tape.")
#调用rewind函数，回到文本的0字节
rewind(current_file)

print("Let's print three lines:")
#以下内容可使用循环
current_line = 1
print_a_line(current_line, current_file)         #打印1，文本的一行

current_line = current_line + 1
print_a_line(current_line, current_file)         #打印2，文本的一行

current_line = current_line + 1
print_a_line(current_line, current_file)         #打印3，文本的一行
