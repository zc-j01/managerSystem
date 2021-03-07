# -*- coding:utf-8 -*-

class Students:
    def __init__(self, name, nums, gender):
        self.name = name
        self.nums = nums
        self.gender = gender


    def __str__(self):
        return "姓名：%s\n性别：%s\n学号：%s" % (self.name, self.gender, self.nums)


