def scan(a):
    sentence = []
    words = a.split()

    for i in words:
        i = i.lower()

        if i in ('north', 'south', 'east'):     #接收到"north south east"时,结果为 [('direction', 'north'),('direction', 'south'),('direction', 'east')]
            word = ('direction', i)
            sentence.append(word)
        elif i in ('go', 'kill', 'eat'):        #以下同理，添加(类型, 词)至sentence中
            word = ('verb', i)
            sentence.append(word)
        elif i in ('the', 'in', 'of'):
            word = ('stop', i)
            sentence.append(word)
        elif i in ('bear', 'princess'):
            word = ('noun', i)
            sentence.append(word)
        elif i.isdigit():
            i = int(i)
            word = ('number', i)
            sentence.append(word)
            i = str(i)
        else:
            word = ('error', i)
            sentence.append(word)

    print(sentence)
    return sentence
