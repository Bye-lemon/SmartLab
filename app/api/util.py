import feedparser
import markdown
import os
import requests

from bs4 import BeautifulSoup
from flask import current_app

RSSURL = "https://rsshub.app/linkedkeeper/index"
BANNERRSS = "http://www.lieyunwang.com/newrss/feed.xml"


def rss_parser(part):
    rss = feedparser.parse(RSSURL)
    part = int(part)
    doc = rss.entries[(part-1)*8: part*8]
    if len(doc) == 0:
        return dict(success=False, msg="没有更多的文章了，再回顾一下前面的吧~")
    list = []
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
    for item in doc:
        r = requests.get(item.link, headers=headers)
        div = BeautifulSoup(r.text, "lxml").find(class_="gray fl")
        keys = [a.string.replace('\u0026', ',') for a in div.find_all("a")]
        key = ','.join(keys)
        string = [str for str in div.strings]
        raw_date = string[-1].replace('\n', '').strip()
        date = raw_date[0:4] + '-' + raw_date[5:7] + '-' + raw_date[-3:-1]
        list.append(dict(name=item.title, link=item.link, keys=key, date=date))
    raw_string = dict(success=True, msg='', news_list=list)
    return raw_string


def linked_parser(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
    r = requests.get(url, headers=headers)
    html = r.text
    soup = BeautifulSoup(html, "lxml")
    raw_md = soup.find(id="js_detail")["value"]
    md = markdown.markdown(raw_md)
    raw_md = dict(success=True, msg='', html=md)
    return raw_md


def banner_parser():
    doc = feedparser.parse(BANNERRSS).entries[:5]
    if len(doc) == 0:
        return dict(success=False, msg='Server Error')
    list = []
    for item in doc:
        soup = BeautifulSoup(item.summary, "lxml")
        img = soup.find("img")["src"]
        list.append(dict(name=item.title, link=item.link, image=img))
    raw_news_list = rss_parser(part="1")
    news_list = raw_news_list["news_list"]
    raw_string = dict(success=True, msg='', banner_list=list, news_list=news_list)
    return raw_string


def lieyun_parser(url):
    doc = feedparser.parse(BANNERRSS).entries[:5]
    for item in doc:
        if item.link == url:
            return dict(success=True, msg='', html=item.summary)
    return dict(success=False, msg="Not Found")


def dir_path_parser():
    path = os.path.join(current_app.root_path, 'static/resource')
    file_list = []
    files = os.listdir(path)
    for file in files:
        file_byte = os.path.getsize(os.path.join(path, file))
        file_size = str(round((float(file_byte) / (1024 * 1024)), 2)) + ' MB'
        file_list.append(
            dict(name=file, size=file_size, link="http://140.143.186.223/static/resource/" + file))
    return dict(success=True, msg='', file_list=file_list)
