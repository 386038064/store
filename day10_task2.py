class cooker:
    __name=''
    __age=0

    def getname(self,name):
        self.__name=name

    def setname(self):
        return self.__name

    def getage(self,age):
        self.__age=age

    def setage(self):
        return self.__age

    def rice(self):
        print('蒸饭')
class  cooker1(cooker):
    def cook(self):
        print ('炒菜')

class cooker1a(cooker1):
    def rice(self):
        print ('蒸饭1')

    def cook(self):
        print ('炒菜1')

cook=cooker1a()
cook.getname('小王')
cook.getage(22)
print('name:',cook.setname(),'age:',cook.setage())
cook.cook()
cook.rice()