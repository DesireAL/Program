from sys import argv
from os.path import exists

csript, from_file, to_file = argv

#print(f"Copying from {from_file} to {to_file}.")

#We could do these two on one line, how?
#in_file = open(from_file, encoding = 'utf-8')                                   #打开需要复制的文件
#indata = in_file.read()                                                         #将复制文件的内容输入到indata中
indata = open(from_file, encoding = 'utf-8').read()                             #二合一

#print(f"The input file is {len(indata)} bytes long")

#print(f"Does the output file exist? {exists(to_file)}")
#print("Ready, hit RETURN to continue, CTRL-C to abort.")
#input("?")

out_file = open(to_file, 'w', encoding = 'utf-8')                               #打开需要粘贴的文件
out_file.write(indata)                                                          #写入indata中的内容

print("Alright, all done.")

out_file.close()
#in_file.close()
