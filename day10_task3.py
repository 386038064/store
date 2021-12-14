class humen:
    __age=0
    __name=''
    __sex=''

    def getage(self,age):
        self.__age=age

    def setage(self):
        return self.__age

    def getname(self,name):
        self.__name=name

    def setname(self):
        return self.__name

    def getsex(self,sex):
        self.__sex=sex

    def setsex(self):
        return self.__sex

class work(humen):
    def work(self):
        print ('干活')

class student(work):
    __num=0

    def study(self):
        print ('学习')

    def sing(self):
        print ('唱歌')

