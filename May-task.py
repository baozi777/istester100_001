# """
# 冒泡法
# """
# b = [9,7,8,6,4,5,3,2,1]
# count = 0
# count_swap = 0
# lenth = len(b)
# for i in range(lenth):
#   flag = False
#   for j in range(lenth-i-1):
#       count+=1
#       if b[j] > b[j+1]:
#           tem = b[j]
#           b[j] = b[j+1]
#           b[j+1] = tem
#           flag = True#有交换过，状态改变
#           count_swap+=1
#   if not flag:#标记优化提升效率
#       break
# print(b,count_swap,count)

# """
# 求十万内的素数，并打印运算次数，运算时间，正确情况下效率越高越好
# """
# print(2)
# count = 1
# sum = 0
# import time
# start = time.perf_counter()
# for i in range(3,100000,2):#进入循环的都是奇数
#     for n in range(3,int(i**0.5)+1,2):#奇数除偶数不能整除，所以跳过
#         sum += 1
#         if i % n == 0 :
#             break
#     else:
#         print(i)
#         count+=1
# end = time.perf_counter()
# print('一共有%d个素数'%count)
# print('算了%d次'% sum)
# print('run:%ss'%(end-start))
# """
# 汉诺塔
# """
# def move(n,a,b,c):
#     if n == 1:
#         print(a, '-->', c)
#     else:
#         move(n - 1, a, c, b)
#         print(a, '-->', c)
#         move(n - 1, b, a, c)
# move(3,'A','B','C')
"""
要求：
类名、属性名、属性类型、方法名，方法参数、方法返回值自拟
自己写main函数测试设计是否合理
1.设计一个‘狗’类
1）属性
颜色
奔跑的速度（单位是m/s）
性别
体重（单位是kg）
2）行为
吃：每吃一次，体重增加0.5kg，输出吃完后的体重
吠（叫）：输出所有的属性
跑：每跑一次，体重减少0.5kg，输出速度和跑完后的体重

2.设计一个‘学生’类
1）属性
姓名、生日、年龄、身高（m）、体重（kg）
性别、C语言成绩、OC成绩、IOS成绩
2）行为
跑步：每跑步一次，身高增加1cm，体重减小0.5kg，输出跑完后的体重
吃饭：每吃一次，身高增加1cm。体重增加0.5kg，输出吃完后的体重
学习：每学习一次，3科成绩各加1分，输出学习完后的3科成绩
睡觉：输出所有的属性

计算总分：算出3科成绩的总分并显示
计算平均分：算出3科成绩的平均分并显示
"""


"""
正则表达式
"""
# #1.匹配所有的开头字母内容
# s="i love you not because of who you are, but because of who i am when i am with you"
# import re
# list1 = re.findall(r"\b\w",s)
# print(list1)
# #\b:匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
#
# #2.匹配所有开头的数字内容
# s="i love you not because 12df 56ere55 6667888 r777 yy88"
# import re
# list1 = re.findall(r"\b\d+",s)
# print(list1)
# #\d+ 为贪婪匹配，把后面符合的数字都匹配出来了

# # 3.匹配出合法的身份证号码（15 或 18位，最后一个可能是字符X）
# s= "1234578457845 d124568745421212 123456789123456 78978978978978978d 12345789654789854X 784568785X123456 123456789123456789 1234567891231232119 1234566879545215458X"
# import re
# list1 = re.findall(r'(\b\d{15}\b)|(\b\d{18}\b)|(\b\d{17}X)',s)
# print(list1)

# # 4.写一个正则表达式判断一个字符串是否是ip地址
# # 规则：一个ip地址由4个数字组成，每个数字之间用.连接。每个数字的大小是0-255 例如：255.189.10.37 正确 256.189.89.9 错误
# import re
# re_str = r'((\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])'
# result = re.fullmatch(re_str,'100.183.10.37')
# print(result)

# # 5. 计算一个字符串中所有的数字的和
# # 例如：字符串是：‘hello90abc 78sjh12.5’ 结果是90+78+12.5 = 180.5
# import re
# str1 = 'hello90abc 78sjh12.5'
# result = re.findall(r'[^a-z]+',str1)#[^...]	表示不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
# print(result)
# sum1 = 0
# for item in result:
#     sum1 += float(item)
# print(sum1)

# # 6. 验证输入的内容只能是汉字
# import re
# re_str = r'[\u4E00-\u9fa5]+'
# s = input('请输入：')
# result = re.fullmatch(re_str,s)
# if result == None:
#     print('输入错误，只能输入汉字')
# else:
#     print(result)