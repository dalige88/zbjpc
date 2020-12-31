# -*- coding:utf-8 -*-

import requests
import json

# 列表
url_list = "http://aiqicha.baidu.com/s?q=%E9%87%8D%E5%BA%86%E9%9C%86%E8%BE%BE%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&t=0"
# 详情
url_details ="https://aiqicha.baidu.com/company_detail_"

listdata_=[]

# 获取数据
def get_page(urls):
    
    headers = {
        "Host":"aiqicha.baidu.com",
        "Connection":"close",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        #"Accept":" text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Referer":urls,
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",

    }
    reponse = requests.get(urls,headers=headers)
    # print(reponse.text)
    return reponse.text

# 获取返回字段
def GetData():
    html=get_page(url_list)
    html=html.split("window.pageData = ")
    

    list_json_data=html[1].split("}};\n\n")
    list_data = list_json_data[0]+"}}"
    list_dt = json.loads(list_data)
    
    pid = list_dt["result"]["resultList"][0]["pid"]

    print(pid)


    ############################ 查询详情 ############################ 
    details_html= get_page(url_details+str(pid))
    details_html = details_html.split("window.pageData = ")

    details_json_data=details_html[1].split("}]};")
    details_data = details_json_data[0]+"}]}"
    details_dt = json.loads(details_data)

    # pid = list_dt["result"]
    # print(details_dt["result"]["describe"])
    # print(details_dt["result"]["telephone"])
    # print(details_dt["result"]["addr"])
    # print(details_dt["result"]["email"])
    # print(details_dt["result"]["website"])
    # print(details_dt["result"]["entName"])

    
    describe = details_dt["result"]["describe"]
    telephone = details_dt["result"]["telephone"]
    addr = details_dt["result"]["addr"]
    email = details_dt["result"]["email"]
    website = details_dt["result"]["website"]
    entName = details_dt["result"]["entName"]

    listdata_01 = [entName, describe, addr, telephone, email, website]

    listdata_.append(listdata_01)


    
    print(listdata_)

    return html


GetData()















