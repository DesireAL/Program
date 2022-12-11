import random   #导入 random 模块
from urllib.request import urlopen  #导入 urlopen 模块中的 urllib.request
import sys      #导入 sys 模块

WORD_URL = "https://learncodethehardway.org/words.txt"  #将链接字符串赋予WORD_URL
WORDS = []  #创建一个名为WORDS的空列表

PHRASES = { #创建一个名为PHRASES的字典
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",    #创建一个叫%%%的类，它是%%%的一种
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** params.", #类%%%有一个__init__，它接收self和***作为参数
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.", #类%%%有一个函数，它接收self和@@@作为参数
    "*** = %%%()":
        "Set *** to an instance of class %%%.", #将***设为类%%%的一个实例
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",    #从***中找到***函数，并使用self和J参数调用它
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."   #从***中获取***属性，并将其设为***
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english": #判断是否有两个参数且第二个参数是否为"english"
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines(): #urllib.request.urlopen()函数用于实现对目标url的访问,
    WORDS.append(str(word.strip(), encoding = 'utf-8')) #将通过readlines获取到的字符串添加进WORDS的列表中
#print(WORDS)
#print(urlopen(WORD_URL).readlines())   #readlines()，是把一个文档的每一行（包含行前的空格，行末加一个\n），作为列表的一个元素，存储在一个list中。每一个行作为list的一个元素。

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(','.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
