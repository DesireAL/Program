def break_words(stuff): #将stuff中的句子切分成独立的单词
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):  #排序words中的所有单词
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):  #弹出第一个词，将其附给变量word并打印
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):  #弹出最后一个词，将其服给变量word并打印
    """Prints the last word after poping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):  #将句子切分并排序
    """Take in a full sentence and returns the sorted words."""
    words = break_words(sentence)  #words为被切分后的句子
    return sort_words(words)  #返回切分后且排序后的句子

def print_first_and_last(sentence):  #打印句子的第一个和最后一个词
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):  #打印重新排序后句子的第一个和最后一个词
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(words)
    print_first_word(words)
    print_last_word(words)
