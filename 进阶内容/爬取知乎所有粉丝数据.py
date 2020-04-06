'''
爬取知乎所有粉丝数据.py
@Author : su 
@Time   : 2020/04/06 20:42:47
'''
import requests
import json
import pymysql
import time

def crawl():
    followers_data = []
    for offset in range(2500, 3000, 20):
        time.sleep(1)
        url = "https://www.zhihu.com/api/v4/columns/NewsFlash/followers?include=data%5B*%5D.follower_count%2Cgender%2Cis_followed%2Cis_following&offset=" + \
            str(offset)+"&limit=20"
        print(url)
        headers = {
            "user-agent: Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) "
            "AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1"
        }
        response = requests.get(url, headers=headers)
        followers_data += response.json().get("data")
    return followers_data

def data_insert(followers_data):
    #打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "db_python")
    #使用cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    val = []
    for dic in followers_data:
        item = (dic['id'], dic['name'], dic['url'],dic['gender'], dic['avatar_url'], dic['follower_count'])
        val.append(item)
    sql = "INSERT INTO t_follow (id, name, url, gender, avatar_url, follower_count) VALUES (%s,%s,%s,%s,%s,%s) "
    try:
        #执行sql语句，批量插入
        cursor.executemany(sql, val)
        #提交数据库执行
        db.commit()
    except:
        #如果发生错误则回滚
        db.rollback()
    finally:
        #关闭数据库
        db.close()


if __name__ == "__main__":
    list = crawl
    print(list)
    data_insert(list)


    