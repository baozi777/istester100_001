"""
2020-06-01 Python 打卡
1、根据下面运行流程图和提示，实现文字版图书管理功能。
提示：主体流程代码已实现如下，三个功能分别用函数来实现.
每本图书用一个字典来存储：book1 ={'id':编号，'name':书名，'location':位置}
所有的图书放在一个列表：books =[book1,book2,book3..............]
主要运用知识点：字典和列表的增删查相关操作， for循环  while循环
基本要求：
实现添加、删除、显示所有书籍的功能函数。
添加图书时：不用考虑书名、编号、位置是否和已有的书籍信息重复：
删除图书时：输入删除的书籍，找到名为书籍的所有数据，显示出来，然后用户根据编号选择删除。
扩展要求：添加图书时，书名和位置可以随便写，编号不能和已经添加过得数据重复
"""

class Book(object):  # 定义一个书类
    def __init__(self,id,name,location):
        self.id = id
        self.name = name
        self.location = location
        return 'ID: %s 书名：<<%s>> 位置: %s' % (self.id,self.name,self.location)
class BookManage(object):
    books = []
    def start(self):
        self.books.append(Book(1,'Python',abc001))
        self.books.append(Book(2,'C++',abb002))
        self.books.append(Book(3,'软件测试的艺术',qwe111))


