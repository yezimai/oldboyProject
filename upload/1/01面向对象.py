#python的面向对象
a = 'aaa'
type(a)

#类的定义
class Animal:
    #pass
    '''animal  class  '''
    eye = 2
    leg = []
    def __init__(self,name,food,color='yellow'):  #__init__  类的初始化函数
        self.name = name
        #self.food = food
        self._food = food
        #self.color = color
        self.__color = color
    def paly(self):
        print('lalala')
    def get_name(self):
        print('%s'%self.name)

#小黄人
minions = Animal('minions','banana')  #实例化
#self.name = minions.name
dog = Animal('旺财','bone')

#类的实例化 基本形式：实例对象名 = 类名（参数）
#在实例化的过程中，self代表的就是这个实例对象自己。

#类属性
minions.leg.append(2)
dog.leg.append(4)

#实例属性
#dog.color = 'red'

###实例的属性相当于实例自己的，类属性相当于公共的

#类的私有变量

#一个_
#dog._food

#两个__
dog._Animal__color
#dog._Animal__color = 'red'

#更多的是一种规范/约定，不没有真正达到限制的目的  最好不要去改私有属性


class People(Animal):
    #pass
    def __init__(self,weight):
        Animal.__init__(self,'xiaoming','apple')
        self.weight = weight
    def paly(self):
        #Animal.paly(self)
        super().paly()
        print('hahaha')


#xm = People('xiaoming','apple')
xm = People(57)
#xm.get_name()
xm.paly()


"""
总结：
1.类的定义
2.类的属性和方法
3.类的实例
4.类继承
"""






















