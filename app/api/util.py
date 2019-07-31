# coding=utf-8
import datetime
import feedparser
import markdown
import os
import requests
from bs4 import BeautifulSoup
from flask import current_app
from requests_html import HTMLSession

RSSURL = "http://www.linkedkeeper.com/home/index.action"
BANNERRSS = "http://www.lieyunwang.com/newrss/feed.xml"
HEADERS = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}


def rss_parser(part):
    part = int(part)
    session = HTMLSession()
    r = session.get(RSSURL, headers=HEADERS)
    list = []
    try:
        tds = r.html.find('td')[(part - 1) * 8: part * 8]
    except:
        tds = r.html.find('td')[(part - 1) * 8:]
    if len(tds) == 0:
        return dict(success=False, msg="没有更多的文章了，再回顾一下前面的吧~")
    for td in tds:
        title = td.find('.blog_weight')
        link = r"http://www.linkedkeeper.com" + title[0].attrs["href"]
        date = str(datetime.date.today().year) + '-' + '-'.join(
            td.find('dd')[2].text.replace('月', ' ').replace('日', '').split())
        tags = ','.join([tag.text for tag in td.find('a[href*="tag"]')])
        list.append(
            dict(name=title[0].text, link=link, keys=tags, date=date))
    raw_string = dict(success=True, msg='', news_list=list)
    return raw_string


def linked_parser(url):
    session = HTMLSession()
    r = session.get(url, headers=headers)
    raw_md = r.find("#js_detail").attrs["value"]
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
