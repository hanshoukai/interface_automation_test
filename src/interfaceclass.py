# /usr/bin/env python
# coding=utf-8
import re
from framework.src.Requestclass import Webrequests

class InterfaceTest():
    def testsearch(self,url,params,headers,requ_method,chinkoption,types,sheet,i,logg):
        r = Webrequests()
        # logg = log()
        if requ_method == "GET":
            R = r.get(url,params=params,headers=headers)
            # return R
        elif (requ_method == "POST" and types == "Form"):
            R = r.post(url,params=params,headers=headers)
            # return R
        elif (requ_method == "POST" and types == "Json"):
            R = r.post_json(url,params=params,headers=headers)
            # return R
        else:
            print("请求失败，请检查case里的数据是否正确!")

        if re.search(chinkoption,str(R)):
            sheet.cell(row=i,column=11).value = "成功"
            sheet.cell(row=i,column=12).value = str(R)
            logg.info(url+" "+requ_method+types+"成功" + str(R))
            return R
            # print("请求成功！")
        else:
            sheet.cell(row=i,column=11).value = "失败"
            sheet.cell(row=i,column=12).value = str(R)
            logg.error(url+" "+requ_method+types+"失败" + str(R))
            return R
            # print("请求失败！")