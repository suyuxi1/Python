'''
爬取粉丝数.py
@Author : su 
@Time   : 2020/04/06 00:00:57
'''
import requests
import csv
import json


def crawl():
    csvfile = open('./res/data.csv', 'w', newline='')
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
    keys = ['id', 'name', 'url', 'gender', 'avatar_url', 'follower_count']
    writer.writerow(keys)
    for x in range(1000):
        url = "https://www.zhihu.com/api/v4/columns/NewsFlash/followers"
        # 查询参数
        params = {
            "limit": 20,
            "offset": x,
            "include": "data[*].follower_count,gender,is_followed,is_following"
        }
        # 必须制定UA，否则知乎服务器会判定请求不合法
        headers = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) "
            "AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1"
        }
        response = requests.get(url, headers=headers, params=params)
        # print("请求URL：", response.url)
        # print("返回数据：", response.text)
        # 解析返回数据
        i = 1
        for dic in response.json().get("data"):
            writer.writerow([dic['id'], dic['name'], dic['url'],
                             dic['gender'], dic['avatar_url'], dic['follower_count']])
            i += 1
    csvfile.close()


if __name__ == "__main__":
    crawl()
