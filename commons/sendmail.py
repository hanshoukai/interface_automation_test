# /usr/bin/env python
# coding=utf-8
import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.application import MIMEApplication

class SendMail:

    def send_mail(self,title):
        msg=email.mime.multipart.MIMEMultipart()       #生成包含多个邮件体的对象
        msg['from']='hankai1202@163.com'

        msg['to']='809773385@qq.com'

        msg['subject']= title
        content='''
        Hi all，
        这是一封接口自动化测试发送的邮件
        博客：http://www.cnblogs.com/hanxiaobei/
        微信公众号：保密
        带附件
        '''

        #邮件正文
        txt=email.mime.text.MIMEText(content)
        msg.attach(txt)

        #excel附件
        file_path = "D:/pycharm workspace/framework/report/guo.xlsx"
        xlsxpart = MIMEApplication(open(file_path, 'rb').read())
        xlsxpart.add_header('Content-Disposition', 'attachment', filename='guo.xlsx')
        msg.attach(xlsxpart)

        #jpg图片附件
        # img_path = "D:/pycharm workspace/practice/Aaron.png"
        # jpgpart = MIMEApplication(open(img_path, 'rb').read())
        # jpgpart.add_header('Content-Disposition', 'attachment', filename='Aaron.png')
        # msg.attach(jpgpart)

        #发送邮件
        smtp=smtplib
        smtp=smtplib.SMTP()
        # smtp.set_debuglevel(1)#设置为调试模式，console中显示
        smtp.connect('smtp.163.com','25') #链接服务器，smtp地址+端口
        smtp.login('hankai1202@163.com','kai521') #登录，用户名+密码
        smtp.sendmail('hankai1202@163.com','809773385@qq.com',str(msg))   #发送，from+to+内容
        smtp.quit()

# mail = SendMail()
# mail.send_mail('接口自动化测试报告')
