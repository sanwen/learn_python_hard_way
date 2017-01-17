# -*- coding: utf-8 -*-
'''
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So,  you're %r old, %r tall and %r heavy" %(age, height, weight)
'''
# 测试input 和 raw_input
print "please input 2 numbers:",
num_1 = input()
num_2 = raw_input()
print "the inputs are:",
print num_1, num_2,eval(num_2)

# print "%d %d %d" %(num_1, num_2, eval(num_2))
print "%.2F %s %.2F" %(num_1, num_2, eval(num_2))