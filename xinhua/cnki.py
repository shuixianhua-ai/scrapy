#-*- codeing = utf-8 -*-
#@Time : 2021/4/2613:32
#@Author : Bianco
#@File : CNKI_SPIDER4.py
#@Software : PyCharm

from bs4 import BeautifulSoup
import requests
import re
import urllib.request,urllib.error
import xlwt
import random

def main():
    baseurl = "https://kns.cnki.net/kns/brief/brief.aspx?curpage="
    datalist = getData(baseurl)

    savePath = ".\\data\\CNKIdata_jichuyixue_1.xls"
    saveData(datalist, savePath)

findTitle = re.compile(r'<h3 class="title_c"><a href=".*?" target="_blank">(.*?)</a>',re.S)
findAbstract = re.compile(r'<p class="abstract_c">(.*?)</p>',re.S)
findJournal = re.compile(r'<span class="journal">\n<a.*?href=.*?>(.*?)</a>',re.S)
findAuthor = re.compile(r'<span class="author">(.*?)</span>',re.S)
findTime = re.compile(r'<label> 发表时间：(.*?)</label>',re.S)
#findKey = re.compile(r'<a data-key=".*?">(.*?)</a>')

def getData(baseurl):
    datalist = []
    for i in range(1,5):
        print(i)
        url = baseurl + str(i) + "&RecordsPerPage=50&QueryID=22&ID=&turnpage=1&tpagemode=L&dbPrefix=CFLS&Fields=&DisplayMode=custommode&PageName=ASP.brief_default_result_aspx&Param=%e8%a1%8c%e4%b8%9a%e5%88%86%e7%b1%bb%e4%bb%a3%e7%a0%81%3d%271280222%3f%27&isinEn=1&"
        html = askURL(url)


        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_ = "GridRightColumn"):
            data = []
            item = str(item)
            # print(item)

            title = re.findall(findTitle,item)[0]
            title = re.sub('<font class="Mark">', "", title)
            title = re.sub('</font>', "", title)
            title = title.strip()
            # print(title)
            data.append(title)

            abstract = []
            abstract = re.findall(findAbstract,item)[0]
            abstract = re.sub('<font class="Mark">',"",abstract)
            abstract = re.sub('</font>',"",abstract)
            abstract = re.sub('&lt;正&gt;',"",abstract)
            # print(abstract)
            data.append(abstract.strip())

            journal = []
            journal = re.findall(findJournal,item)
            # print(journal)
            data.append(journal)

            author = []
            author = re.findall(findAuthor,item)
            numa = len(author)

            for j in range(0,numa):
                author[j] = re.sub(re.compile(r'<a.*?>'),"",author[j])
                author[j] = re.sub("</a>","",author[j])
            # print(author)
            data.append(author)

            time = []
            time = re.findall(findTime,item)[0]
            time = re.sub('发表时间'," ",time)
            time = re.sub('：', " ", time)
            time = time.strip()
            # print(time)
            data.append(time)

            # print(data)
            datalist.append(data)


    # print(datalist)
    return datalist

def askURL(url):
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46',
        'Accept - Encoding': 'gzip, deflate, br',
        'Accept - Language': 'zh - CN, zh;q = 0.9, en;q = 0.8, en - GB;q = 0.7, en - US;q = 0.6',
        'Cookie': 'Ecp_ClientId=1201128151701993175; Ecp_session=1; ASP.NET_SessionId=pc3ksf5escnryl1y5pkvapbh; SID_kns8=123117; cnkiUserKey=fcc9de8c-4bba-0620-098c-f83a1a5ad0c5; CurrSortFieldType=desc; SID_kns_new=kns123120; SID_kcms=124103; _pk_ref=%5B%22%22%2C%22%22%2C1608008643%2C%22https%3A%2F%2Fwww.cnki.net%2F%22%5D; SID_kxreader_new=011121; SID_kns=025123115; SID_klogin=125141; SID_krsnew=125133; UM_distinctid=17709ba3d41308-0dc0fcbe7d6163-7d677965-fa000-17709ba3d42200; SID_recommendapi=125142; knsLeftGroupSelectItem=; CurrSortField=%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2f(%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2c%27TIME%27); Ecp_ClientIp=222.205.124.99; Ecp_Userid=5001550; Hm_lvt_6e967eb120601ea41b9d312166416aa6=1615553507,1617155864; Hm_lpvt_6e967eb120601ea41b9d312166416aa6=1617157418; amid=c8e20b8b-4f02-4ae7-a5f5-cf27a65bf579; _pk_ref=%5B%22%22%2C%22%22%2C1619523919%2C%22https%3A%2F%2Fwww.cnki.net%2F%22%5D; _pk_ses=*; ASPSESSIONIDASBQSSAS=BLPBNDPDCNDKALCKAJOMCMPD; Ecp_IpLoginFail=210427125.125.36.81; SID_crrs=125132; RsPerPage=50; KNS_SortType=; _pk_id=cc5ebe0f-fc5a-4786-a7af-825b69957132.1610092635.31.1619526381.1619523919.'
    }

    proxiesList = {'http':'http://120.77.215.57:80'}

    #proxy = random.choice(proxiesList)
    # httpproxy_handler = urllib.request.ProxyHandler(proxy)
    # opener = urllib.request.build_opener(httpproxy_handler)

    #request = urllib.request.Request(url, headers=head)

    #request = requests.get(url,headers=head,proxies=proxy)
    request = requests.get(url, headers=head, proxies=proxiesList)

    html = ""
    try:
        #response = urllib.request.urlopen(request)
        #response = opener.open(request)
        #html = response.read().decode("utf-8")

        html = request.text.encode(request.encoding).decode('utf-8')
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

def saveData(datalist, savePath):
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 压缩
    worksheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)  # 每个单元格是否可覆盖
    # 列设定
    col = ("Title", "Abstract", "Journal", "Author", "Time")
    for i in range(0, 5):
        worksheet.write(0, i, col[i])  # 列名

    for k in range(0, 750):
        print("%d"%(k+1))
        data = datalist[k]
        for j in range(0, 5):
            worksheet.write(k+1,j,data[j])

    workbook.save(savePath)

if __name__ == "__main__" :
    main()
    print("success")