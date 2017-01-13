# coding: utf-8
# 导入module sys 中的 argv
from sys import argv

# unpack argv 赋值给 script 和 file_name
script, file_name = argv

# 通过file_name打开文件
txt = open(file_name)

# 打印文件名
print "Here's your file %r." % file_name

# 读取并打印文件内容
print txt.read()

# 再次输入文件名
print "Type the filename again:"

# 接收输入的文件名并打印提示符
file_again = raw_input("> ")
txt_again = open (file_name,"w+")

# 读取file_name对应的文件，解码为utf-8并打印出来
print txt_again.read().decode("utf-8")

# 关闭文件txt
txt.close()

# 测试写文件txt_again
txt_again.write("新的内容")
txt_again.flush()
# 关闭文件txt_again
txt_again.close()

print txt_again.read().decode("gbk")



