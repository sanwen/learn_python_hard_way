#-*- coding:utf-8 -*-

# 打印系统的编码
import sys
print sys.getdefaultencoding()

# 定义一个joke，4个字符串儿构成
x = "there is %d type of people." %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not)

# 打印这个joke
print x
print y

print "I said: %r." % x
print "I also said：'%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# 通过变量打印
print joke_evaluation % hilarious

# 连接两个字符串儿
w = "This is the left side of ..."
e = "a string with a right side."

print w + e
