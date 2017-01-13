# -*-coding:utf-8 -*-

# 汽车的数量
cars = 100
# 汽车的空间
space_in_a_car = 4.0
# 司机数目
drivers = 30
# 乘客的数目
passengers = 90
# 可用车辆
cars_not_driven = cars - drivers
# 在用车辆
cars_driven = drivers
#
carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# python Calculator
i = 3
j = 4
k = 5.0
print 3*3 + 4*4 == 5*5
# flag1 = true is false
flag2 = True
print flag1
print flag2
