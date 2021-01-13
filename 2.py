from urllib import request
from bs4 import BeautifulSoup
import re
import json
import xlwt
import time
import requests
import json
import urllib
from selenium import webdriver

# 下载地址
url_list = []
# 猪八戒列表
# url='https://chongqing.zbj.com/xcxkfzbjzbj/f.html?fr=zbj.sy.zyyw_2nd.lv2'
# 网站推广
url_name='猪八戒服务商'
# url='https://chongqing.zbj.com/wzkf/f.html'

# 最大停止数量
# overnum=4
overnum=9999999999
listdata=[]
# chromedriver_url='F:\chromedriver\chromedriver.exe'
chromedriver_url='chromedriver.exe'



# 写入数据到  EXCEL
def OutExcel(data):

    # # data = comm_DB(sql)
    wb = xlwt.Workbook(encoding='utf-8') # 创建workbook,其实是execl
    style1 = xlwt.XFStyle()  # 设置单元格格式为文本
    style1.num_format_str = '@'

    style2 = xlwt.XFStyle()  # 设置单元格格式为文本
    style2.num_format_str = '@'
    # 设置字体
    font = xlwt.Font()
    # 比如设置字体加粗和下划线
    font.bold = True
    font.underline = True
    style2.font = font

    # 添加一个表
    ws = wb.add_sheet('test')

    # ws.write(0, 2, '店铺名称', style=style2)
    ws.write(0, 0, '类型', style=style2)
    ws.write(0, 1, '公司名称', style=style2)
    ws.write(0, 2, '简介', style=style2)
    ws.write(0, 3, '联系电话 / 邮箱地址', style=style2)
    ws.write(0, 4, '公司官网 / 公司地址', style=style2)


    nums = 1
    for item in data:
        if nums <= len(data):
            # 3个参数分别为行号，列号，和内容
            # 需要注意的是行号和列号都是从0开始的
            # ws.write(nums, 2, item[0], style=style1)
            ws.write(nums, 0, url_name, style=style1)
            ws.write(nums, 1, item[0], style=style1)
            ws.write(nums, 2, item[1], style=style1)
            ws.write(nums, 3, item[2], style=style1)
            ws.write(nums, 4, item[3], style=style1)

            nums = nums + 1


    # 保存excel文件
    file_name = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    file_name = file_name.replace(' ', '')
    file_name = file_name.replace(':', '')

    wb.save('猪八戒'+str(file_name)+'.xls')
    print('文件保存完毕！（猪八戒'+str(file_name)+'.xls）')
    print('等待中....')
	# 清空数据
    # listdata_=[]

# urlss="http://aiqicha.baidu.com/s?q=%E5%93%88%E5%B0%94%E6%BB%A8%E5%9C%A3%E8%9E%8D%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&t=0"
url_es="https://aiqicha.baidu.com/"
# serachName="重庆霆达科技有限公司"
# 调用 chromedriver.exe 模拟人工输入
def GetCookie(serachName):
	# driver = webdriver.Firefox(executable_path = 'bin\geckodriver.exe')
    driver = webdriver.Chrome(executable_path = chromedriver_url)
    driver.get(url_es)
    driver.find_element_by_xpath('//*[@id="aqc-search-input"]').send_keys(serachName)
	# driver.find_element_by_id("su").click()
    driver.find_element_by_class_name("search-btn").click()

    html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
    html = html.split("window.pageData = ")
    print(len(html))
    list_json_data = html[1].split("}};\n\n")
    list_data = list_json_data[0]+"}}"
    list_dt = json.loads(list_data)

    if list_data.find('resultList') < 1:
        return ''

    resultList = list_dt["result"]["resultList"]

    pid = ''
    if len(resultList) > 0:
        pid = resultList[0]["pid"]
	# pid = list_dt["result"]["resultList"][0]["pid"]
    else:
        print("没有找到："+serachName)

	#退出
    driver.close()
    driver.quit()

    print(resultList)
    print("总共：" + len(list_pid) + "，不要慌！还没完，后面还有货....")

	# cookie_s=driver.get_cookies()

	# return cookie_s
    return pid



shequList=[{
	"name":"重庆社区",
	"img":["","",""]
}]
shequName=["重庆社区","南京社区"]
p=0
djpage=0
def glyh(cs):
	cs.replace("'", "\\'")
	cs.replace("\"", "\\'")
	cs.replace("\n", "")
	return cs
def okpa(http) :
	if __name__ == "__main__":
		response = request.urlopen(http)
		html = response.read()
		global p
		p=p+1
		print("当前第"+str(int(djpage))+"页 第"+str(int(p))+"条");
		bf = BeautifulSoup(html,"lxml")
		if bf.find_all("iframe"):
			src = bf.find_all("iframe")[0].attrs['src']
		else:
			src=http
		src=src.replace("https:","")
		src=src.replace("salerinfo.html","")
		response2 = request.urlopen("https:"+src)
		html2 = response2.read()
		bf2 = BeautifulSoup(html2,"lxml")

		if bf2.find_all("h1",class_="title"):
			title = bf2.find_all("h1",class_="title")[0].get_text()		#店铺名称
		elif bf2.find_all("div",class_="w-head-pic"):
			title = bf2.find_all("div",class_="w-head-pic")[0].find('img').attrs['alt']		#店铺名称
		else:
			title = "无"
		print("店铺名称1:"+title)

		if(bf2.find_all("div",class_="info-content")):
			gongsi = bf2.find_all("div",class_="info-content")[0].get_text()		#公司名称	
		else:
			gongsi = "无"
			# address="无"
		gongsi = gongsi.replace("\n","")
		print("公司名称2:"+gongsi)

		gongsi = glyh(gongsi)
		title = glyh(title)
		
		if gongsi != '无':
			listdata.append(gongsi)
		else:
			if title != '无':
				# title = title.decode("utf-8")
				title = title[0:3]
				listdata.append(title)
		

def palist(http):
	if __name__ == "__main__":
		response = request.urlopen(http)
		html = response.read()
		print("开始"+http)
		bf = BeautifulSoup(html,"lxml")
		global djpage
		try:
			listindex=bf.find_all("div",class_="pagination")[0].find_all("li",class_="active")[0].find('a').get_text();
			djpage=listindex
			
		except:
			djpage=1
			
		list=bf.find_all("a",class_="name")
		listlen=len(bf.find_all("a",class_="name"))
		z=0

		for i in list:
			z=z+1

			if z>=listlen:
				
				urls = paindex(http)
				print(urls)
				if urls == "最后一页":
					break
				else:
					palist(paindex(http))
				
			else:
				try:
					i=i.attrs['href'].replace("?fr=djwy", "")
					newurl="https:"+i+"salerinfo.html"
					#print(str(z)+" " + str(listlen));
					okpa(newurl)
				except:
					pass
				
				
			if z>overnum:
				break
		

			

		
def paindex(http):
	if __name__ == "__main__":
		response = request.urlopen(http)
		html = response.read()
		#print("开始");
		bf = BeautifulSoup(html,"lxml")
		
		try:
			listindex=len(bf.find_all("div",class_="pagination")[0].find_all("li"))
			w=0
			for d in range(listindex):
				w=w+1
				t="active"
				s=str(bf.find_all("div",class_="pagination")[0].find_all("li")[d])
				if(t in s):
					break

			list=bf.find_all("div",class_="pagination")[0].find_all("li")
			page=list[w].find("a").attrs['href']					#下一个	
		except:
			listindex=0
			page="javascript:"


		# listindex=len(bf.find_all("div",class_="pagination")[0].find_all("li"));
		w=0
		# for d in range(listindex):
		# 	w=w+1
		# 	t="active"
		# 	s=str(bf.find_all("div",class_="pagination")[0].find_all("li")[d])
		# 	if(t in s):
		# 		break

		# list=bf.find_all("div",class_="pagination")[0].find_all("li")
		# page=list[w].find("a").attrs['href']					#下一个
		
		if "javascript:" in page:
			return "最后一页"
		else:
			return "https://"+http.split("/")[2]+page;







####################  获取爱企查数据  ##############################

listdata_=[]
# 详情
url_details ="https://aiqicha.baidu.com/company_detail_"

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
def GetData(pidlist):
    for pid in pidlist:
		############################ 查询详情 ############################ 		

        driver = webdriver.Chrome(executable_path = chromedriver_url)
        driver.get(url_details+str(pid))
        try:
            entName=driver.find_elements_by_class_name("name")[0].get_attribute('innerText')
            describe=driver.find_elements_by_class_name("content-info-child-brief")[0].get_attribute('innerText')
            telephone_email=driver.find_elements_by_class_name("content-info-child")[0].get_attribute('innerText').strip("编辑企业信息")
            website_addr=driver.find_elements_by_class_name("content-info-child")[1].get_attribute('innerText')
            
            print("邮箱："+telephone_email)
            print("地址："+website_addr)
            
            listdata_01 = [entName, describe, telephone_email, website_addr]
            listdata_.append(listdata_01)
        except:
            print("获取元素报错了....")
            # GetData(pidlist)
            pass
        
        #退出
        driver.close()
        driver.quit()
        time.sleep(10)

    OutExcel(listdata_)



def GteAll(url_s):
	list_pid=[]
	listdata_=[]

	for item in url_s:
		print("314："+item)
		try:
			pids = GetCookie(item)
			if pids != '':
				list_pid.append(pids)
			time.sleep(10)
		except:
			break
		

	print(list_pid)
	GetData(list_pid)
	# OutExcel(listdata_)
	

# 加载下载地址
def GetUrls():
	file = open("urls.txt")
	for line in file:
		url_list.append(line)
	file.close()








# python chromedriver.exe
# ss=['32231383078519', '15886171920049']
# GetData(ss)
GetUrls()
for url in url_list:
	listdata = []
	palist(url)
	# print(len(listdata))
	GteAll(listdata)
