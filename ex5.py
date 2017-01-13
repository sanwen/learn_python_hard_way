# coding:utf-8

# my_name
my_name = 'Zed A. Shaw'
# my_age
my_age = 35 # not a lie
# my_height
my_height = 74 # inches
# my_weight
my_weight = 180 #lbs
# my_eyes
my_eyes = 'blue'
# my_teeth
my_teeth = 'White'
# my_hair
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." %my_weight # note i don't add sapce
print "Actually that's not too heavy."
print "He's got %s eyes and %s  hair" % (my_eyes, my_hair)
print "His teeth are usualy %s depending on the coffee." % my_teeth

# this line is triky ,try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

print "\n"
# --- extra ex ---
# name
name = 'Zed A. Shaw'
# age
age = 35 # not a lie
# height
height = 74 # inches
# weight
weight = 180 #lbs
# eyes
eyes = 'blue'
# teeth
teeth = 'White'
# hair
hair = 'Brown'

print "Let's talk about %s." % name
print "Let's talk about %r." % name
print "He's %d inches tall or %.2f cm tall." % (height, height * 2.54)
print "He's %d pounds heavy or %.2f kg heavy" % (weight, weight * 0.45) # note i don't add sapce
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair" % (eyes, hair)
print "His teeth are usualy %s depending on the coffee." % teeth

# this line is triky ,try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "%.*f" %(2,1.2)

'''
可以用如下的方式，对格式进行进一步的控制：

%[(name)][flags][width].[precision]typecode

(name)为命名

flags可以有+,-,' '或0。+表示右对齐。-表示左对齐。' '为一个空格，表示在正数的左侧填充一个空格，从而与负数对齐。0表示使用0填充。

width表示显示宽度

precision表示小数点后精度
'''

"""
%s    字符串 (采用str()的显示)

%r    字符串 (采用repr()的显示)

%c    单个字符

%b    二进制整数

%d    十进制整数

%i    十进制整数

%o    八进制整数

%x    十六进制整数

%e    指数 (基底写为e)

%E    指数 (基底写为E)

%f    浮点数

%F    浮点数，与上相同

%g    指数(e)或浮点数 (根据显示长度)

%G    指数(E)或浮点数 (根据显示长度)

 

%%    字符"%"
"""
# 默认是右对齐的 +号表示的是加上正负号

print "% d" % -3
print "%-+4d" % -3
print "% d" % 3
print "%+4d" % 3
