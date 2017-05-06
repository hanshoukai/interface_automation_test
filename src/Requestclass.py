# /usr/bin/env python
# coding=utf-8
import requests
import json

class Webrequests():
    def get(self,url,params,headers):
        try:
            r = requests.get(url,params=params,headers=headers)
            json_r = r.json()
            return json_r
        except BaseException as e:
            print("请求失败！",str(e))

    def post(self,url,params,headers):
        try:
            r = requests.post(url,data=params,headers=headers)
            json_r = r.json()
            return json_r
        except BaseException as e:
            print("请求失败！",str(e))

    def post_json(self,url,params,headers):
        try:
            data = params
            data = json.dumps(data)   #python数据类型转化为json数据类型
            r = requests.post(url,data=data,headers=headers)
            #print("获取返回的状态码",r.status_code)
            json_r = r.json()         #print("json类型转化成python数据类型",json_r)
            return json_r
        except BaseException as e:
            print("请求失败！",str(e))
'''
    def post_file(self,url,file_name,headers):
        print("文件上传请求url=",url)
        print("文件文件名=",file_name)
        print("文件上传请求headers=",headers)

        file =  {"file":open(file_name,'rb')} #只读方式打开
        try:
            r = requests.post(url,file=file,headers=headers)
            #可同时提交请求数据和要上传的文件
            # r = requests.post(url,data=data,file=file,headers=headers)

            # status_code = r.status_code  #获取响应状态码
            # requests_headers = r.headers #获取响应头
            response = r.json()
            # print("获取响应内容=",response)
            return response
        except Exception as e:
            print("%s",str(e))
            return {}        #返回空

'''
