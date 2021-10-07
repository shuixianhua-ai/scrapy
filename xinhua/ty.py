import requests  # 发起网络请求
from bs4 import BeautifulSoup  # 解析HTML文本
import pandas as pd  # 处理数据
import os
import time  # 处理时间戳
import json


def fetchUrl(url, kw, page):
    # 请求头
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68",
        "Refer": "http://search.people.cn/s/?keyword=%E6%96%B0%E5%86%A0&st=0&_=1617851359505"
    }

    # 请求参数
    payloads = {
        "endTime": 0,
        "hasContent": True,
        "hasTitle": True,
        "isFuzzy": False,
        "key": "新冠",
        "limit": 10,
        "page": page,
        "sortType": 0,
        "startTime": 0,
        "type": 0,
    }

    # 发起 post 请求
    proxies = {"http": "http://46.4.147.246:1080"}

    #r = requests.post(url, headers=headers, data=json.dumps(payloads), proxies=proxies)
    r = requests.post(url, headers=headers, data=json.dumps(payloads))
    return r.json()


def parseJson(jsonObj):
    # 解析数据
    records = jsonObj["data"]["records"];
    for item in records:
        # 这里示例解析了几条，其他数据项如末尾所示，有需要自行解析

        belongsName = item["belongsName"]

        displayTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item["displayTime"] / 1000))

        title = BeautifulSoup(item["title"], "html.parser").text
        # url = item["url"]

        yield [[title, displayTime, belongsName]]


def saveFile(path, filename, data):
    # 如果路径不存在，就创建路径
    if not os.path.exists(path):
        os.makedirs(path)
    # 保存数据
    dataframe = pd.DataFrame(data)
    dataframe.to_csv(path + filename + ".csv", encoding='utf_8_sig', mode='a', index=False, sep=',', header=False)


if __name__ == "__main__":
    # 起始页，终止页，关键词设置
    start = 2740
    end = 19999
    kw = "test"

    # 保存表头行
    headline = [["标题", "发表时间", "来源"]]
    saveFile("./data/", kw, headline)
    # 爬取数据
    for page in range(start, end + 1):
        url = "http://search.people.cn/api-search/elasticSearch/search"
        html = fetchUrl(url, kw, page)
        for data in parseJson(html):
            saveFile("./data/", kw + "0", data)
        print("第{}页爬取完成".format(page))

    # 爬虫完成提示信息
    print("爬虫执行完毕！数据已保存至以下路径中，请查看！")
    print(os.getcwd(), "\\data")
