# "1. 列表、字符串、元组、字典之间的相互转换"
# print("1.列表、字符串、元组、字典之间的相互转换")
# str1 = "hello world"
# list1 = [11, 22, 33, 44]
# list2 = ['aa', 'bb', 'cc', 'dd']
# tuple1 = (1, 2, 3, 4)
# dict1 = {'name': 'zhangsan', 'age': 18, 'gender': 'boy'}
# print('字符串转列表：',list(str1))
# print('字符串转列表：',str1.split())
# print("元组转列表：",list(tuple1))
# print("字典转列表",list(dict1.keys()))
# print("字典转列表：",list(dict1.values()))
# print("字符串转元组",tuple(str1))
# print("列表转元组：",tuple(list1))
# print("两个数组合并成一个字典：",dict(zip(list1, list2)))
# print("列表转字符串：",''.join(list2))
# print("字符串转字典：dict = eval(str)")
# print(str(list1))
# print(type(str(list1)))
#
# "2.列表的遍历方式"
# print("2.列表的遍历方式")
# #列表的增加元素list.append('haha') 默认增加到末尾
# #列表插入元素到指定位置list.insert(i,'add') i为索引
# #列表删除元素list.pop（）删除末尾元素，list.pop(i)删除索引为i的元素,list.remove(haha)直接删除这个元素
# #替换元素 list[i] = 'haha' 替换索引为i的元素
# print('方法一')
# for i in list2:
#     print(i)
#
# print('方法二')
# for i in range(0,int(len(list2))):
#     print(list2[i])
#
# print('方法三')
# i = 0
# while i < int(len(list2)):
#     print(list2[i])
#     i += 1
#
#
# "3. 字符串截取子串"
# print("3. 字符串截取子串")
# str1 = 'aaabbbcccdddeeefff'
# print('字符串截取子串：',str1[3:9])
# print('字符串截取子串：',str1[::3])
# print('字符串截取子串：',str1[-1:-7:-1])
#
# "4. 字典的遍历方式"
# print("4. 字典的遍历方式")
# # 字典的遍历方式
# dict1 = {'name': 'zhangsan', 'age': 18, 'gender': 'boy'}
#
# print('***打印key***')
# for i in dict1.keys():
#     print(i)
#
# print('***打印value***')
# for i in dict1.values():
#     print(i)
#
# print('***打印(key,value)***')
# for i in dict1.items():
#     print(i)
#
# print('***打印key:value***')
# for k,v in dict1.items():
#     print(k,':',v)
#
# "5-字典的增加、删除、更新"
# print("5-字典的增加、删除、更新")
# # 字典的增加、删除、更新
# dict1 = {'name': 'zhangsan', 'age': 18, 'gender': 'boy'}
#
# dict1['Class'] = 'First'
# print('新增后的字典：',dict1)
#
# dict1['age'] = 16
# print('更新后的字典：',dict1)
#
# del dict1['name']   # 删除键name
# print('del删除后的字典：',dict1)
#
# dict1.clear()    #清空字典
# print('clear清空后的字典：',dict1)
# """
# 6. 请输入考试分数，并判断考试成绩的等级
#     score >= 85 A
#     score >= 75 B
#     score >= 60 C
#     score >= 40 D
#     score >= 0 E
# """
# def inputfloat(score ="请输入您的分数:"):
#     while True:
#         data = input(score)
#         try:
#             inputData = eval(data) #去除字符串的引号
#             if type(inputData) == float or int:
#                 # break
#                 return inputData
#         except:
#             print('输入错误')
#             pass
# if __name__ == "__main__":
#     score = inputfloat()
#     if score >= 85:
#         print("A")
#     elif score >= 75:
#         print('B')
#     elif score >= 60:
#         print('C')
#     elif score >= 40:
#         print('D')
#     elif score >= 0:
#         print('E')
#     else:
#         print('输入成绩应为0-无限大')
#
# """
# 输入一个五位数，请判断是否为回文数
# """
# num = int(input("请输入一个五位数:"))
# num1 = str(num)
# if len(num1) != 5:
#     print('输入的不是五位数')
# elif num1[0]==num1[4] and num1[1]==num1[3]:
#     print(num,'是个回文数')
# else:
#     print(num,'不是回文数')
#
# """
# 1、 用户登陆程序需求:
#     1. 输入用户名和密码;
#     2. 判断用户名和密码是否正确? (name='root', passwd='westos')
#     3. 为了防止暴力破解， 登陆仅有三次机会， 如果超过三次机会， 提示错误次数过多，账号已被冻结
# """
# n = 1
# while n <= 3:
#     name = input('请输入你的用户名：')
#     password = input('请输入你的密码：')
#     if name == 'root' and password == 'westos':
#         print('登录成功')
#         break
#     n=n+1
# else:
#     print('输入错误次数过多，账号已被冻结')
#
# """
# 2、使用了 while 来计算 1 到 100 的总和
# """
# n =1
# sum = 0
# while n <=100:
#     sum = sum +n
#     n = n + 1
# print(sum)

#"打印乘法表"
#间距一样
# for i in range(1,10):
#     # print(' '*8*(i-1),end='')
#     for j in range(1,i+1):
#         product = i *j
#         if j > 1 and product <10:#这个范围的积是个位数
#             product = ' '+str(product) #补空格
#         else:
#             product = str(product)
#         print('%d*%d=%s\t'%(i,j,product),end='')
#         # print('{0}*{1}={2}\t'.format(i,j,product),end='')#\t横向制表符
#     print()

# """
# 1、剪刀石头布游戏：
# 游戏开始，输入数字表示选项：退出【0】石头【1】剪刀【2】布【3】
# 游戏结束，计算游戏者的胜率
# 提示：人机游戏，机器可随机出拳
# """
# import random
# print('游戏开始，输入数字表示选项：退出[0]石头[1]剪刀[2]布[3]')
# count =0
# sum =0
# shenglv =0
# rand = random.randint(1,4)
# num = int(input('输入你的选项：\n'))
# print('机器出拳',rand)
# while num != 0:
#     if (num,rand) in [(1,2),(2,3),(3,1)]:
#         count += 1
#         sum += 1
#     else:
#         sum += 1
#     num = int(input('请输入你的选项：\n'))
#     rand = random.randint(1,3)
#     print('机器出拳',rand)
# if sum == 0:
#     shenglv = 0
# else:
#     shenglv = count / sum
# print(count,sum)
# print('你一共玩了%d局，胜率为%.2f%%' % (sum,shenglv*100))

"""
封装一个计算器函数
计算器功能：仅支持加减乘除运算
转载https://blog.csdn.net/a971956955/article/details/81489914
"""

import re


def eq_format(eq):
    '''
    :param eq: 输入的算式字符串
    :return: 格式化以后的列表，如['60','+','7','*','8']
    '''
    format_list = re.findall('[\d\.]+|\(|\+|\-|\*|\/|\)', eq)
    return format_list


def change(eq, count):
    '''
    :param eq: 刚去完括号或者乘除后的格式化列表
    :param count: 发生变化的元素的索引
    :return: 返回一个不存在 '+-' ,'--'类的格式化列表
    '''
    if eq[count] == '-':
        if eq[count - 1] == '-':
            eq[count - 1] = '+'
            del eq[count]
        elif eq[count - 1] == '+':
            eq[count - 1] = '-'
            del eq[count]
    return eq


def remove_multiplication_division(eq):
    '''
    :param eq: 带有乘除号的格式化列表
    :return: 去除了乘除号的格式化列表
    '''
    count = 0
    for i in eq:
        if i == '*':
            if eq[count + 1] != '-':
                eq[count - 1] = float(eq[count - 1]) * float(eq[count + 1])
                del (eq[count])
                del (eq[count])
            elif eq[count + 1] == '-':
                eq[count] = float(eq[count - 1]) * float(eq[count + 2])
                eq[count - 1] = '-'
                del (eq[count + 1])
                del (eq[count + 1])
            eq = change(eq, count - 1)
            return remove_multiplication_division(eq)
        elif i == '/':
            if eq[count + 1] != '-':
                eq[count - 1] = float(eq[count - 1]) / float(eq[count + 1])
                del (eq[count])
                del (eq[count])
            elif eq[count + 1] == '-':
                eq[count] = float(eq[count - 1]) / float(eq[count + 2])
                eq[count - 1] = '-'
                del (eq[count + 1])
                del (eq[count + 1])
            eq = change(eq, count - 1)
            return remove_multiplication_division(eq)
        count = count + 1
    return eq


def remove_plus_minus(eq):
    '''
    :param eq: 只带有加减号的格式化列表
    :return: 计算出整个列表的结果
    '''
    count = 0
    if eq[0] != '-':
        sum = float(eq[0])
    else:
        sum = 0.0
    for i in eq:
        if i == '-':
            sum = sum - float(eq[count + 1])
        elif i == '+':
            sum = sum + float(eq[count + 1])
        count = count + 1
    if sum >= 0:
        eq = [str(sum)]
    else:
        eq = ['-', str(-sum)]
    return eq


def calculate(s_eq):
    '''
    :param s_eq: 不带括号的格式化列表
    :return: 计算结果
    '''
    if '*' or '/' in s_eq:
        s_eq = remove_multiplication_division(s_eq)
    if '+' or '-' in s_eq:
        s_eq = remove_plus_minus(s_eq)
    return s_eq


def simplify(format_list):
    '''
    :param format_list: 输入的算式格式化列表如['60','+','7','*','8']
    :return: 通过递归去括号，返回简化后的列表
    '''

    bracket = 0  # 用于存放左括号在格式化列表中的索引
    count = 0
    for i in format_list:
        if i == '(':
            bracket = count
        elif i == ')':
            temp = format_list[bracket + 1: count]
            # print(temp)
            new_temp = calculate(temp)
            format_list = format_list[:bracket] + new_temp + format_list[count + 1:]
            format_list = change(format_list, bracket)  # 解决去括号后会出现的--  +- 问题
            return simplify(format_list)  # 递归去括号
        count = count + 1
    return format_list  # 当递归到最后一层的时候，不再有括号，因此返回列表


def caculator(eq):
    format_list = eq_format(eq)
    s_eq = simplify(format_list)
    ans = calculate(s_eq)
    if len(ans) == 2:
        ans = -float(ans[1])
    else:
        ans = float(ans[0])
    return ans

if __name__ == '__main__':
    equation = '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
    ans = caculator(equation)
    print('eval运算结果：', eval(equation))
    print('程序运算结果：', ans)