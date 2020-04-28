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