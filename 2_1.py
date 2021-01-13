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
    print("不要慌！还没完，后面还有货....")

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



def GteAll():
	list_pid=['55633951959199', '31765292336021', '20484480715179', '10686377320785', '29667146828953', '33640102136471', '36309482144477', '69441552744182', '15703451192583', '61052741864679', '13214369128629', '66151913845307', '55633951959199', '27488123889826', '26808001634107', '31196850915073', '10611001390252', '53921297689469', '14691852635232', '31380609066222', '20484480715179', '11073308587068', '29524934311323', '62821721622799', '64676526613167', '89954530029324', '33927970014124', '19080302314819', '18985968142197', '55765332169167', '30202894388264', '33489716504014', '25124311383734', '55942052896272', '30331206085812', '29961701114718', '10281741138930', '29381242079026', '11842355825368', '89401481293236', '29713248614336', '14705042559431', '10799027822937', '24807545199820', '11126923653672', '11540592303797', '39432216009107', '11041826311106', '32231383078519', '55633951959199', '31765292336021', '20484480715179', '10686377320785', '30392382728726', '21684507168710', '19272210098424', '30392382728726', '29381242079026', '29713248614336', '11842355825368', '11259301775367', '62821721622799', '30202894388264', '29886318555954', '27488123889826', '30719531082636', '30331206085812', '26982268537216', '14705042559431', '66151913845307', '10611001390252', '29912731211520', '30696361198535', '39502621520876', '72792409038502', '53921297689469', '26519809024711', '20484480715179', '14705042559431', '13742078422385', '34720091839950', '31380609066222', '11126923653672', '18985968142197', '16150452821420', '13214369128629', '11126923653672', '14691852635232', '74324968342949', '26808001634107', '22586269491016', '10774986087036', '11073308587068', '29667146828953', '29982377656133', '21869401530582', '29524934311323', '39432216009107', '30331206085812', '30331206085812', '29912731211520', '39502621520876', '72792409038502', '53921297689469', '26519809024711', '30696361198535', '13742078422385', '34720091839950', '31380609066222', '14705042559431', '18985968142197', '16150452821420', '13214369128629', '11126923653672', '14691852635232', '11126923653672', '20484480715179', '26808001634107', '10774986087036', '11073308587068', '74324968342949', '29982377656133', '21869401530582', '29524934311323', '39432216009107', '30331206085812', '29667146828953', '19080302314819', '89954530029324', '64676526613167', '33489716504014', '29667146828953', '10774986087036', '25124311383734', '89401481293236', '26282297869436', '19272210098424', '74324968342949', '33640102136471', '31196850915073', '55765332169167', '19918682062630', '55633951959199', '10799027822937', '55942052896272', '10952162986438', '22676893084979', '64512739462428', '10686377320785', '20484480715179', '31765292336021', '55633951959199', '34982662741660', '13742078422385', '34720091839950', '31380609066222', '18985968142197', '16150452821420', '14705042559431', '13214369128629', '11126923653672', '14691852635232', '20484480715179', '11126923653672', '26808001634107', '10774986087036', '11073308587068', '29982377656133', '21869401530582', '74324968342949', '29524934311323', '39432216009107', '30331206085812', '19080302314819', '89954530029324', '29667146828953', '64676526613167', '33489716504014', '25124311383734', '29667146828953', '89401481293236', '10774986087036', '26282297869436', '19272210098424', '74324968342949', '33640102136471', '31196850915073', '55765332169167', '19918682062630', '55633951959199', '10799027822937', '55942052896272', '10952162986438', '22676893084979', '64512739462428', '24807545199820', '31124244354677', '55633951959199', '31765292336021', '10686377320785', '20484480715179', '30392382728726', '29381242079026', '29713248614336', '30331206085812', '19080302314819', '89954530029324', '64676526613167', '74324968342949', '33489716504014', '25124311383734', '29667146828953', '89401481293236', '19272210098424', '29667146828953', '74324968342949', '33640102136471', '31196850915073', '55765332169167', '19918682062630', '10774986087036', '55633951959199', '10799027822937', '10952162986438', '22676893084979', '64512739462428', '24807545199820', '31124244354677', '54401598927874', '29798866109820', '32295648813150', '23327710739133', '11291053519835', '35385100235762', '46764306171675', '11520118840636', '55633951959199', '20484480715179', '10686377320785', '31765292336021', '30392382728726', '29381242079026', '29713248614336', '11842355825368', '11259301775367', '27488123889826', '26982268537216', '14705042559431', '72792409038502', '26519809024711', '30331206085812', '13742078422385', '31380609066222', '16150452821420', '29667146828953', '31196850915073', '55765332169167', '19918682062630', '55633951959199', '10799027822937', '10774986087036', '22676893084979', '64512739462428', '24807545199820', '31124244354677', '54401598927874', '29798866109820', '32295648813150', '23327710739133', '11291053519835', '35385100235762', '19102402241235', '72963712236635', '43602391672313', '26373219177469', '31986168824185', '31765292336021', '55633951959199', '20484480715179', '10686377320785', '30392382728726', '29381242079026', '11842355825368', '27488123889826', '11259301775367', '26982268537216', '72792409038502', '26519809024711', '13742078422385', '30331206085812', '16150452821420', '13214369128629', '11126923653672', '14691852635232', '30696361198535', '20484480715179', '26808001634107', '10774986087036', '11073308587068', '14705042559431', '29524934311323', '39432216009107', '30331206085812', '19080302314819', '14705042559431', '11126923653672', '64676526613167', '33489716504014', '25124311383734', '29667146828953', '19272210098424', '74324968342949', '74324968342949', '33640102136471', '55765332169167', '10799027822937', '22676893084979', '29667146828953', '64512739462428', '24807545199820', '31124244354677', '54401598927874', '29798866109820', '10774986087036', '32295648813150', '35385100235762', '72963712236635', '43602391672313', '26373219177469', '30699855873323', '32182182302528', '29134724608230', '77237284852094', '33927970014124', '83514596471316', '69441552744182', '47335314537899', '10035265907018', '50273716299178', '55633951959199', '20484480715179', '26808001634107', '10774986087036', '11073308587068', '74324968342949', '29524934311323', '39432216009107', '30331206085812', '19080302314819', '14705042559431', '10774986087036', '64676526613167', '33489716504014', '25124311383734', '29667146828953', '19272210098424', '74324968342949', '33640102136471', '55765332169167', '22676893084979', '64512739462428', '24807545199820', '31124244354677', '54401598927874', '29798866109820', '35385100235762', '26373219177469', '30699855873323', '32182182302528', '77237284852094', '33927970014124', '83514596471316', '69441552744182', '21906579005122', '10281741138930', '36309482144477', '11540592303797', '21684507168710', '50511485467262', '37477729758230', '29040316487149', '55633951959199', '20484480715179', '10686377320785', '31765292336021', '25124311383734', '10774986087036', '29667146828953', '19272210098424', '74324968342949', '33640102136471', '55765332169167', '22676893084979', '64512739462428', '24807545199820', '31124244354677', '29798866109820', '35385100235762', '33927970014124', '83514596471316', '69441552744182', '21906579005122', '10281741138930', '36309482144477', '11540592303797', '21684507168710', '37477729758230', '50511485467262', '30354272235548', '80598825729322', '36891927052843', '10701002628137', '47608310095247', '29761834901955', '34425917672425', '10686377320785', '31765292336021', '20484480715179', '55633951959199', '30392382728726', '68422923281216', '30201732475351', '56012597555971', '23727555751309', '10585416120005', '40001165476101', '29650265212497', '55633951959199', '20484480715179', '31765292336021', '10686377320785', '29381242079026', '27488123889826', '13742078422385', '11259301775367', '31380609066222', '16150452821420', '13214369128629', '11126923653672', '14691852635232', '11126923653672', '20484480715179', '26808001634107', '10774986087036', '11073308587068', '74324968342949', '29524934311323', '39432216009107', '30331206085812', '14705042559431', '64676526613167', '14705042559431', '33489716504014', '25124311383734', '19272210098424', '74324968342949', '33640102136471', '10774986087036', '55765332169167', '22676893084979', '64512739462428', '31124244354677', '35385100235762', '83514596471316', '10281741138930', '10686377320785', '20484480715179', '29381242079026', '27488123889826', '13742078422385', '11259301775367', '31380609066222', '16150452821420', '13214369128629', '11126923653672', '14691852635232', '11126923653672', '20484480715179', '26808001634107', '10774986087036', '11073308587068', '74324968342949', '30331206085812', '14705042559431', '64676526613167', '33489716504014']

	GetData(list_pid)
	# OutExcel(listdata_)
	

GteAll()






