"1. 列表、字符串、元组、字典之间的相互转换"
print("1.列表、字符串、元组、字典之间的相互转换")
str1 = "hello world"
list1 = [11, 22, 33, 44]
list2 = ['aa', 'bb', 'cc', 'dd']
tuple1 = (1, 2, 3, 4)
dict1 = {'name': 'zhangsan', 'age': 18, 'gender': 'boy'}
print('字符串转列表：',list(str1))
print('字符串转列表：',str1.split())
print("元组转列表：",list(tuple1))
print("字典转列表",list(dict1.keys()))
print("字典转列表：",list(dict1.values()))
print("字符串转元组",tuple(str1))
print("列表转元组：",tuple(list1))
print("两个数组合并成一个字典：",dict(zip(list1, list2)))
print("列表转字符串：",''.join(list2))
print("字符串转字典：dict = eval(str)")
print(str(list1))
print(type(str(list1)))

"2.列表的遍历方式"
print("2.列表的遍历方式")
#列表的增加元素list.append('haha') 默认增加到末尾
#列表插入元素到指定位置list.insert(i,'add') i为索引
#列表删除元素list.pop（）删除末尾元素，list.pop(i)删除索引为i的元素,list.remove(haha)直接删除这个元素
#替换元素 list[i] = 'haha' 替换索引为i的元素
print('方法一')
for i in list2:
    print(i)

print('方法二')
for i in range(0,int(len(list2))):
    print(list2[i])

print('方法三')
i = 0
while i < int(len(list2)):
    print(list2[i])
    i += 1


"3. 字符串截取子串"
print("3. 字符串截取子串")
str1 = 'aaabbbcccdddeeefff'
print('字符串截取子串：',str1[3:9])
print('字符串截取子串：',str1[::3])
print('字符串截取子串：',str1[-1:-7:-1])

"4. 字典的遍历方式"
print("4. 字典的遍历方式")
# 字典的遍历方式
dict1 = {'name': 'zhangsan', 'age': 18, 'gender': 'boy'}

print('***打印key***')
for i in dict1.keys():
    print(i)

print('***打印value***')
for i in dict1.values():
    print(i)

print('***打印(key,value)***')
for i in dict1.items():
    print(i)

print('***打印key:value***')
for k,v in dict1.items():
    print(k,':',v)

"5-字典的增加、删除、更新"
print("5-字典的增加、删除、更新")
# 字典的增加、删除、更新
dict1 = {'name': 'zhangsan', 'age': 18, 'gender': 'boy'}

dict1['Class'] = 'First'
print('新增后的字典：',dict1)

dict1['age'] = 16
print('更新后的字典：',dict1)

del dict1['name']   # 删除键name
print('del删除后的字典：',dict1)

dict1.clear()    #清空字典
print('clear清空后的字典：',dict1)
"""
6. 请输入考试分数，并判断考试成绩的等级
    score >= 85 A
    score >= 75 B
    score >= 60 C
    score >= 40 D
    score >= 0 E
"""
def inputfloat(score ="请输入您的分数:"):
    while True:
        data = input(score)
        try:
            inputData = eval(data) #去除字符创的引号
            if type(inputData) == float or int:
                # break
                return inputData
        except:
            print('输入错误')
            pass
if __name__ == "__main__":
    score = inputfloat()
    if score >= 85:
        print("A")
    elif score >= 75:
        print('B')
    elif score >= 60:
        print('C')
    elif score >= 40:
        print('D')
    elif score >= 0:
        print('E')
    else:
        print('输入成绩应为0-无限大')

"""
输入一个五位数，请判断是否为回文数
"""
num = int(input("请输入一个五位数:"))
num1 = str(num)
if len(num1) != 5:
    print('输入的不是五位数')
elif num1[0]==num1[4] and num1[1]==num1[3]:
    print(num,'是个回文数')
else:
    print(num,'不是回文数')

"""
1、 用户登陆程序需求:
    1. 输入用户名和密码;
    2. 判断用户名和密码是否正确? (name='root', passwd='westos')
    3. 为了防止暴力破解， 登陆仅有三次机会， 如果超过三次机会， 提示错误次数过多，账号已被冻结
"""
n = 1
while n <= 3:
    name = input('请输入你的用户名：')
    password = input('请输入你的密码：')
    if name == 'root' and password == 'westos':
        print('登录成功')
        break
    n=n+1
else:
    print('输入错误次数过多，账号已被冻结')

"""
2、使用了 while 来计算 1 到 100 的总和
"""
n =1
sum = 0
while n <=100:
    sum = sum +n
    n = n + 1
print(sum)