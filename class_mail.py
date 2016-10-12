#coding:utf-8
class mail():
    def __init__(self):
        self.id=''            # id
        self.sender=''        #发件者邮箱
        self.password=''      #密码
        self.receiver=''      #收件人邮箱
        self.theme=''         #主题
        self.content=''       #内容
        self.state=''         #状态
    def setId(self,id):       #封装Id
        self.id=id
    def setSender(self,sender):#封装发件人
        self.sender=sender
    def setPassword(self,password):#封装密码
        self.password=password
    def setReceiver(self,receiver):#封装收件人
        self.receiver=receiver
    def setTheme(self,theme):      #封装主题
        self.theme=theme
    def setContent(self,content):  #封装内容
        self.content=content
    def setState(self,state):      #封装状态
        self.state=state
    def getId(self):               #获取Id
        return self.id
    def getSender(self):           #获取发件人
        return self.sender
    def getPassword(self):         #获取密码
        return self.password
    def getReceiver(self):         #获取收件人
        return self.receiver
    def getTheme(self):            #获取主题
        return self.theme
    def getContent(self):          #获取内容
        return self.content
    def getState(self):            #获取状态
        return self.state