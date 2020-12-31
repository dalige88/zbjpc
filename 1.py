from urllib import request
from bs4 import BeautifulSoup
import re
import json
import xlwt
import time

# 最大停止数量
overnum = 40
listdata = []

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
    ws.write(0, 1, '公司名称', style=style2)
    ws.write(0, 2, '简介', style=style2)
    ws.write(0, 3, '公司地址', style=style2)
    ws.write(0, 4, '营业执照', style=style2)
    ws.write(0, 5, '数据源地址', style=style2)
    ws.write(0, 6, '公司logo', style=style2)

	
    nums = 1
    for item in data:
        if nums <= len(data):
            # 3个参数分别为行号，列号，和内容
            # 需要注意的是行号和列号都是从0开始的
            # ws.write(nums, 2, item[0], style=style1)
            ws.write(nums, 1, item[1], style=style1)
            ws.write(nums, 2, item[2], style=style1)
            ws.write(nums, 3, item[3], style=style1)
            ws.write(nums, 4, item[4], style=style1)
            ws.write(nums, 5, item[5], style=style1)
            ws.write(nums, 6, item[6], style=style1)

            # print(item[2])
            nums = nums + 1


    # 保存excel文件
    file_name = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    file_name = file_name.replace(' ', '')
    file_name = file_name.replace(':', '')

    wb.save('猪八戒'+str(file_name)+'.xls')
    print('文件保存完毕！（猪八戒'+str(file_name)+'.xls）')
    print('等待中....')





shequList = [{
	"name" : "重庆社区",
	"img" : ["", "", ""]
}]
shequName=["重庆社区","南京社区"]
p=0
djpage=0
fileName="data.sql"
def glyh(cs):
	cs.replace("'", "\\'")
	cs.replace("\"", "\\'")
	return cs
def okpa(http) :
	if __name__ == "__main__":
		response = request.urlopen(http)
		html = response.read()
		global p
		p=p+1
		print("当前第"+str(int(djpage))+"页 第"+str(int(p))+"条");
		print(http);
		bf = BeautifulSoup(html,"lxml")
		if bf.find_all("iframe"):
			src = bf.find_all("iframe")[0].attrs['src']
		else:
			src=http
		src=src.replace("https:","")
		src=src.replace("salerinfo.html","")
		#print(bf.find_all("div",class_="fix-im-cate")[0].get_text())
		response2 = request.urlopen("https:"+src)
		html2 = response2.read()
		bf2 = BeautifulSoup(html2,"lxml")
		if bf2.find_all("img",id="head-img"):
			img=bf2.find_all("img",id="head-img")[0].attrs['src']		#头像地址
		elif bf2.find_all("div",class_="w-head-pic"):
			img=bf2.find_all("div",class_="w-head-pic")[0].find('img').attrs['src']		#头像地址
		else:
			img="无"
		if bf2.find_all("h1",class_="title"):
			title=bf2.find_all("h1",class_="title")[0].get_text()		#店铺名称
		elif bf2.find_all("div",class_="w-head-pic"):
			title=bf2.find_all("div",class_="w-head-pic")[0].find('img').attrs['alt']		#店铺名称
		else:
			title="无"
		print("店铺名称1:"+title)

		if(len(bf2.find_all("div",class_="no-about"))>0):
			jianjie="暂无店铺介绍"
		elif bf2.find_all("pre",class_="content-item morestatus content-item-info1"):
			jianjie= bf2.find_all("pre",class_="content-item morestatus content-item-info1")[0].get_text()		#公司简介
		elif bf2.find_all("p",class_="introduce-company-msg"):
			jianjie=bf2.find_all("p",class_="introduce-company-msg")[0].get_text()
		else:
			jianjie="无"
		print(jianjie)

		if(bf2.find_all("div",class_="info-content")):
			gongsi=bf2.find_all("div",class_="info-content")[0].get_text()		#公司名称	
			address=bf2.find_all("div",class_="info-content")[3].get_text()		#公司地址
		else:
			gongsi="无"
			address="无"
		print("公司名称2:"+gongsi)
		print("公司地址2:"+address)

		fuwuarray=[]
		if(bf2.find_all("div",class_="category-item")):
			fuwu=bf2.find_all("div",class_="category-item")		#公司服务
			for o in fuwu:
				fuwuarray.append(o.get_text())				#存储为数组
		else:
			fuwuarray.append("无")
		if(bf2.find_all("img",class_="certificate-img lazy")):	
			yingye = bf2.find_all("img",class_="certificate-img lazy")[0].attrs['data-original'];		#营业执照
		else:
			yingye="无"
		shequAddress=""
		sname=""
		sphone=""
		if(bf2.find_all("a",class_="zworks-item")):
			shequlen=len(bf2.find_all("a",class_="zworks-item"))
			shequ=bf2.find_all("a",class_="zworks-item")[0]
			sqName=shequ.get_text();			#社区名字
			sqsrc = shequ.attrs['href']     	#社区地址
			response3 = request.urlopen(sqsrc)
			html3 = response3.read()
			bf3 = BeautifulSoup(html3,"lxml")
			gwimg=[]
			gwimgList=bf3.find_all("img",style="width:100%;height: 100%;")
			shequList = bf3.find_all("div",class_="info-form-head-right")
			bsq=[] #社区用户信息
			# for d in shequList:
			# 	sname=d.find("div",class_="head-title").get_text()
			# 	sphone=d.find("div",class_="head-title-phone").get_text()
			# 	a={}
			# 	a['name']=sname
			# 	a['phone']=sphone
			# 	bsq.append(a)
				
			# if bf3.find_all("p",class_="zwork-positon"):
			# 	shequAddress=bf3.find_all("p",class_="zwork-positon")[0].get_text()		#社区地址
			# else:
			# 	shequAddress="无"
			# for i in gwimgList:
			# 	gwimg.append(i.attrs['src'])
		else:
			sqsrc="无"
			sqName="无"
			gwimg=""
			bsq=""

		# print("社区用户信息")
		# print(sname)
		# print(sphone)



		
		'''
		for i in range(shequlen):
			shequ=bf2.find_all("a",class_="zworks-item")[i]
			sqName=shequ.get_text();
			if sqName in shequName:
				dqshequ.append(sqName)
			else:
				dqshequ.append(sqName)
				shequName.append(sqName)
		'''
		img=glyh(img)
		bsq=json.dumps(bsq)
		title=glyh(title)
		jianjie=glyh(jianjie)
		gongsi=glyh(gongsi)
		address=glyh(address)
		yingye=glyh(yingye)
		shequAddress=glyh(shequAddress)
		sqName=glyh(sqName)
		sqsrc=glyh(sqsrc)


		listdata_01=[
			title,
			gongsi,
			jianjie,
			address,
			yingye,
			glyh(url),
			img,

		]
		listdata.append(listdata_01)
		
		if len(listdata)==overnum:
			print(listdata)
			OutExcel(listdata)
			# print(listdata[0])
			# dt=listdata[0]
			# print(dt[0])
			# for target_list in listdata[0]:
			# 	print(target_list)
			# return


		# sql='INSERT INTO `gongsi`.`gsinfo` SET `title`="'+title+'",`jianjie`="'+jianjie+'",`gsname`="'+gongsi+'",`address`="'+address+'",`yingye`=\''+yingye+'\',`fuwu`=\''+json.dumps(fuwuarray)+'\',`url`=\''+glyh(url)+'\',`logo`="'+img+'",`shequ`="'+sqName+'",`shequUser`=\''+bsq+'\',`shequAddress`="'+shequAddress+'",`shequimg`=\''+json.dumps(gwimg)+'\';'
		# with open(fileName,'a',encoding='utf-8') as f:    #设置文件对象
		# 	f.write(sql)                 #将字符串写入文件中
def palist(http):
	if __name__ == "__main__":
		response = request.urlopen(http)
		html = response.read()
		print("开始"+http);
		bf = BeautifulSoup(html,"lxml")
		global djpage
		listindex=bf.find_all("div",class_="pagination")[0].find_all("li",class_="active")[0].find('a').get_text();
		djpage=listindex
		list=bf.find_all("a",class_="name")
		listlen=len(bf.find_all("a",class_="name"))
		z=0
		for i in list:
			z=z+1
			
			
			if z>overnum:
				return



			if z>=listlen:
				palist(paindex(http))
				print(paindex(http));
			else:
				i=i.attrs['href'].replace("?fr=djwy", "")
				newurl="https:"+i+"salerinfo.html";
				#print(str(z)+" " + str(listlen));
				okpa(newurl)
def paindex(http):
	if __name__ == "__main__":
		response = request.urlopen(http)
		html = response.read()
		#print("开始");
		bf = BeautifulSoup(html,"lxml")
		listindex=len(bf.find_all("div",class_="pagination")[0].find_all("li"));
		w=0
		for d in range(listindex):
			w=w+1
			t="active"
			s=str(bf.find_all("div",class_="pagination")[0].find_all("li")[d])
			if(t in s):
				break

		list=bf.find_all("div",class_="pagination")[0].find_all("li")
		page=list[w].find("a").attrs['href']					#下一个
		return "https://"+http.split("/")[2]+page;
# url = input("输入爬取的列表地址：")
# fileName = input("输入保存的文件名称(例如：data.sql)：")

url='https://chongqing.zbj.com/xcxkfzbjzbj/f.html?fr=zbj.sy.zyyw_2nd.lv2'
fileName = '123.sql'
palist(url);
