import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):                                      #后面带井号的均可在直接执行主要语句时注释掉
    line = language_file.readline()                                             #
    if line:                                                                    #
        print_line(line, encoding, errors)                                      #
        return main(language_file, encoding, errors)                            #



def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("ex23_languages.txt", encoding = "utf-8")

main(languages, encoding, error)                                                #

#取消定义main函数，直接执行主要语句
#line = 1
#while line:
#    line = languages.readline()
#    if line:        #判断line是否为空，为空则不再打印
#        print_line(line, encoding, error)
