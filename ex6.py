#-*- coding:utf-8 -*-

# ��ӡϵͳ�ı���
import sys
print sys.getdefaultencoding()

# ����һ��joke��4���ַ���������
x = "there is %d type of people." %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not)

# ��ӡ���joke
print x
print y

print "I said: %r." % x
print "I also said��'%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# ͨ��������ӡ
print joke_evaluation % hilarious

# ���������ַ�����
w = "This is the left side of ..."
e = "a string with a right side."

print w + e
