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

