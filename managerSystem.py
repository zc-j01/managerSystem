# -*- coding:utf-8 -*-
import os
import time
from student import *
from pandas import DataFrame
import pandas as pd

data = {"姓名": [], "性别": [], "学号": []}


class ManagerSystem:
    def __init__(self):
        self.students_list = []
        # [student1,student2]将对象存在list中

    def run(self):
        # 加载数据
        self.load_data()
        flag = 1
        if flag:
            flag = int(input("欢迎进入学员管理系统。请选择：\n1.进入系统\n0.退出系统\n:"))
            while flag:
                # 功能菜单
                print('1:添加学员')
                print('2:删除学员')
                print('3:修改学员信息')
                print('4:查询学员信息')
                print('5:显示所有学员信息')
                print('6:保存学员信息')
                print('7:退出系统')
                option = input('请选择以上功能:')
                if option != '7':
                    if option == '1':
                        self.add_student()
                    elif option == '2':
                        self.del_student()

                    elif option == '3':
                        self.modify_student()
                    elif option == '4':
                        self.seek()
                    elif option == '5':
                        self.display()
                    elif option == '6':
                        self.save()
                    else:
                        print("%s无对应功能，请重新输入:" % option)
                else:
                    # 退出程序
                    flag = 0
                time.sleep(2)  # 延迟2秒方便查看数据

    def add_student(self):
        name = input("请输入学员姓名：")
        nums = input("请输入学员学号：")
        gender = input("请输入学员性别：")
        student = Students(name, nums, gender)
        self.students_list.append(student)

    def del_student(self):
        tmp = self.seek(flag='del')
        indx = int(input("请输入你要删除学员的序号:"))
        try:
            self.students_list.remove(tmp[indx - 1])
        except IndexError:
            print("输入序号不存在。")

    def modify_student(self):
        tmp = self.seek(flag='modify')

        indx = int(input("请输入你要修改学员的序号:"))
        try:
            self.students_list.remove(tmp[indx - 1])
        except IndexError:
            print("输入序号不存在。")
        print("请输入该名学员的新信息")
        new_name = input("姓名:")
        new_gender = input("性别:")
        new_nums = input("学号:")
        student = Students(new_name, new_nums, new_gender)
        self.students_list.append(student)

    def seek(self, flag='seek'):
        """查找到所有满足要求的学员并返回列表"""
        tmp = []
        if flag == 'del':
            name = input("请输入需要删除学员的姓名：")
        elif flag == 'modify':
            name = input("请输入需要修改学员的姓名：")
        else:
            name = input("请输入需要查找学员的姓名：")
        order = 0
        for stu in self.students_list:
            if stu.name == name:
                order += 1
                tmp.append(stu)
                print(order, end='.')
                print(stu)
        print("共找到%d名学员。" % len(tmp))
        return tmp

    def display(self):
        for each in self.students_list:
            print(each)

    def save(self):
        with open("./info.csv", 'a') as fp:
            for each in self.students_list:
                global data
                data["姓名"].append(each.name)
                data["性别"].append(each.gender)
                data["学号"].append(each.nums)
            df = DataFrame(data)
            df.to_csv("./info.csv", encoding="utf_8_sig")
            data = {"姓名": [], "性别": [], "学号": []}

    def load_data(self):
        if not os.path.exists("./info.csv"):
            print("文件不存在。请将文件存于该程序目录下！")
        else:
            df = pd.read_csv("./info.csv")
            for i in range(len(df)):
                student = Students(df["姓名"][i], df["学号"][i], df["性别"][i])
                self.students_list.append(student)
