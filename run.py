# /usr/bin/env python
# coding=utf-8
import sys
sys.path.append("D:/pycharm workspace/")
from framework.src.Traversal_testcase import run_case
from framework.commons.sendmail import SendMail

test_case = "D:/pycharm workspace/framework/testcase/laohuanglitestcase3.xlsx"
save_case = "D:/pycharm workspace/framework/report/guo.xlsx"
run = run_case()
run.runcase(test_case,save_case)

# sendmail = SendMail()
# sendmail.send_mail(title)
