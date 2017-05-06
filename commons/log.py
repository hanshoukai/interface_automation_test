# /usr/bin/env python
# coding=utf-8
import logging

class log():
    def __init__(self):
        self.logger = logging.getLogger("mylogger")
        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:
            # 创建一个handler，将log写入文件中
            fh = logging.FileHandler('D:/pycharm workspace/framework/log/log.txt',mode='w')
            fh.setLevel(logging.INFO)

            # 再创建一个handler，将log输出在控制台
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            # 设置输出格式
            log_format = "%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s"
            formatter = logging.Formatter(log_format)
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            #把handler添加到logger里，其实可以理解为汇报给大领导
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)


    def info(self,content):
        self.logger.info(content)

    def error(self,content):
        self.logger.error(content)


'''
class Logcat():
    def outputlog(self,log):
        # 创建一个logger
        logger = logging.getLogger("mylogger")
        logger.setLevel(logging.INFO)

        # 创建一个handler，将log写入文件中
        fh = logging.FileHandler('D:/pycharm workspace/framework/log/log.txt','w')
        fh.setLevel(logging.INFO)

        # 再创建一个handler，将log输出在控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 设置输出格式
        log_format = "%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s"
        formatter = logging.Formatter(log_format)
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        #把handler添加到logger里，其实可以理解为汇报给大领导
        logger.addHandler(fh)
        logger.addHandler(ch)
        logger.critical(log)

# q = Logcat()
# data = "jinsd"
# q.outputlog(data)

'''