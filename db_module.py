#coding=utf-8
import MySQLdb
from class_mail import mail
class dbmodule(object):
    def __init__(self):     #初始化数据库相关数据
        self.mysqlIP = '127.0.0.1'
        self.mysqlUser = 'root'
        self.mysqlPWD = ''

    #参数：邮件类
    def saveToHigeGrade(self,mail):  #保存数据到高等级数据库
        tablestr="insert into email values('"+mail.getId()+"','"+mail.getSender()+"','"+mail.getPassword()+"','"+mail.getReceiver()+"','"+mail.getTheme()+"','"+mail.getContent()+"','"+mail.getState()+"')"
        self.cur.execute(tablestr)

    # 参数：邮件类
    def saveToMiddleGrade(self, mail):#保存数据到中等级数据库
        tablestr = "insert into email values('" + mail.getId() + "','" + mail.getSender() + "','" + mail.getPassword() + "','" + mail.getReceiver() + "','" + mail.getTheme() + "','" + mail.getContent() + "','" + mail.getState() + "')"
        self.cur.execute(tablestr)

    # 参数：邮件类
    def saveToLowGrade(self, mail):  #保存数据到低等级数据库
        tablestr = "insert into email values('" + mail.getId() + "','" + mail.getSender() + "','" + mail.getPassword() + "','" + mail.getReceiver() + "','" + mail.getTheme() + "','" + mail.getContent() + "','" + mail.getState() + "')"
        self.cur.execute(tablestr)
    def openHighDb(self):            #打开高等级数据库的游标
        try:
            self.dbName = 'High'
            self.cur = MySQLdb.connect(self.mysqlIP, self.mysqlUser, self.mysqlPWD, self.dbName,
                                       autocommit=True,
                                       charset='utf8',
                                       use_unicode=True).cursor(MySQLdb.cursors.DictCursor)
            self.cur.execute(
                "create table email(id text ,sender text,password text,receiver text,theme text,content text,state text)")
        except:
            print ""

    def openMiddleDb(self):#打开中等级数据库的游标
        try:
            self.dbName = 'Middle'
            self.cur = MySQLdb.connect(self.mysqlIP, self.mysqlUser, self.mysqlPWD, self.dbName,
                                       autocommit=True,
                                       charset='utf8',
                                       use_unicode=True).cursor(MySQLdb.cursors.DictCursor)
            self.cur.execute(
                "create table email(id text ,sender text,password text,receiver text,theme text,content text,state text)")
        except:
            print ""

    def openLowDb(self): #打开低等级数据库的游标
        try:
            self.dbName = 'Low'
            self.cur = MySQLdb.connect(self.mysqlIP, self.mysqlUser, self.mysqlPWD, self.dbName,
                                       autocommit=True,
                                       charset='utf8',
                                       use_unicode=True).cursor(MySQLdb.cursors.DictCursor)
            self.cur.execute(
                "create table email(id text ,sender text,password text,receiver text,theme text,content text,state text)")
        except:
            print ""

        #参数：安全等级 （字符串）
        #返回值：查询结果的列表
        #{'sender': u'zl_al@126.com', 'state': u'anquan', 'content': u'test', 'theme': u'hello', 'receiver': u'zhanglei@126.com', 'password': u'zhanglei', 'id': u'1'}
    def selectEmail(self,state):  #根据安全等级筛选数据，返回查询数据
        tableStr="select * from email where state = \""+state+"\""
        result=self.cur.execute(tableStr)
        info = self.cur.fetchmany(result)
        for i in info:
            self.updateDate(i)
        return info
    #参数：字典列表
    def updateDate(self,info):#根据状态把已处理过得邮件状态改成已处理
        str=info.get("state")
        self.cur.execute("update email set state='yichuli' where state = "+"\""+str+"\"")




