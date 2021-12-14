import time
class oldphone:
    __paizi=''

    def getpaizi(self,paizi):
        self.__paizi=paizi

    def setpaizi(self):
        return self.__paizi

    def call(self,num):
        print ('正在给',num,'打电话')

class  newphone(oldphone):
    def call(self,num):
        print ('语音拨号中')
        for i in range(5):
            print ('。',end='')
            time.sleep(1)
        super(newphone, self).call(num)
    def introduce(self):
        print('品牌为：',self.setpaizi(),'的手机很好用...')
my=newphone()
my.getpaizi('华为')
my.introduce()
my.call(13222)
