# -*- coding:utf-8 -*-

import requests



url = "http://aiqicha.baidu.com/s?q=%E9%87%8D%E5%BA%86%E9%9C%86%E8%BE%BE%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&t=0"
# 获取数据
def get_page():
    
    headers = {
        "Host":"aiqicha.baidu.com",
        "Connection":"close",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        #"Accept":" text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Referer":"https://aiqicha.baidu.com/s?q=%E9%87%8D%E5%BA%86%E9%9C%86%E8%BE%BE%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&t=0",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
        "Cookie":"BIDUPSID=328EFFCC08C21AFC6BC420CECA552BA1; PSTM=1600050953; BDUSS=2lzTTdwNVlieEtEQWEzZmJiSWIySDd0NVR2SVE4TnFTTVFpNXUxUGtjdlNtfjVmRVFBQUFBJCQAAAAAAAAAAAEAAAAiBOhDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANIO11~SDtdfM; BDUSS_BFESS=2lzTTdwNVlieEtEQWEzZmJiSWIySDd0NVR2SVE4TnFTTVFpNXUxUGtjdlNtfjVmRVFBQUFBJCQAAAAAAAAAAAEAAAAiBOhDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANIO11~SDtdfM; __yjs_duid=1_f143bf8e2fbcd3e483b302ed6dd1b3931608865882032; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID=E6FD67F0B408C7E6BE122F4DE51CFB3F:FG=1; H_PS_PSSID=1424_33241_33306_31253_33284_33350_33313_33312_33311_33310_33309_26350_33308_33307_33266_33389_33385_33370; MCITY=-132%3A; BDSFRCVID=sl4OJexroG3S8fTrgdEPUl83ZawSOejTDYLEOwXPsp3LGJLVJeC6EG0Ptfzq-d_-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tR3aQ5rtKRTffjrnhPF3KP73XP6-hnjy3b7gVnQm-J3fsfJah5A5W4_W0Pn-aq3RymJ42-39LPO2hpRjyxv4y4Ldj4oxJpOJ5jQDsRb7Hl51fbbvbURvD--g3-AqBM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIE3-oJqC_BhI8G3f; BDPPN=d3f1137466818f005bc5ce7a5da7b99a; Hm_lvt_baca6fe3dceaf818f5f835b0ae97e4cc=1609297400; log_guid=4356e02b385f5a4004909931b24b1a43; delPer=0; PSINO=6; BAIDUID_BFESS=E6FD67F0B408C7E6BE122F4DE51CFB3F:FG=1; yjs_js_security_passport=1e6b13ed4a8c40a4cc6918c248bc97ffc3bfaa78_1609315357_js; _fb537_=xlTM-TogKuTwVZO148cZH%2ApP3O9ngEecWqOHDUbSz0mFmd; Hm_lpvt_baca6fe3dceaf818f5f835b0ae97e4cc=1609320123; ab_sr=1.0.0_NGIwNzFjNjQ5MzNiZWEzOWM2MDNlYWMwYzhmMzNkMzdjMzg0MGMyYjZhOTI2ZGJhZTY5NWM1Y2NhMjFhYWNmZmRjZmJiNTE4NmUyZWI4NjliMmY3YzQ4ZWFhZTFkZDQ4; __yjsv5_shitong=1.0_7_41529dfd7ae98ec859e02fd62537feb75b2b_300_1609320120389_183.67.51.15_4e3044f8",

    }
    reponse = requests.get(url,headers=headers)
    # print(reponse.text)
    return reponse.text

# 获取返回字段
def GetData():
    html=get_page()
    html=html.split('<script>')
    print(html)
    return html


GetData()















