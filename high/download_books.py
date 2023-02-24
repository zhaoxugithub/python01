"""
类说明:下载《笔趣看》网小说: url:https://www.biqukan.com/
Parameters:
	target - 《笔趣看》网指定的小说目录地址(string)
Returns:
	无
Modify:
	2017-05-06
"""
import os
import re
import sys
from urllib import request

import requests
from bs4 import BeautifulSoup


class download(object):
    def __int__(self, target):
        self.__target_url = target
        self.__head = {}

    """
    函数说明:获取下载链接
    Parameters:
    	无
    Returns:
    	novel_name + '.txt' - 保存的小说名(string)
    	numbers - 章节数(int)
    	download_dict - 保存章节名称和下载链接的字典(dict)
    Modify:
    	2017-05-06
    """

    def get_download_url(self):
        # 忽略大小写匹配正则
        charter = re.compile(u'[第](.+)章', re.IGNORECASE)
        target_req = requests.Request(url=self.__target_url, headers=self.__head)
        target_response = request.urlopen(target_req)
        target_html = target_response.read().decode('gbk', 'ignore')
        listmain_soup = BeautifulSoup(target_html, 'lxml')

        pass


def Writer(self, name, path, text):
    pass


def Downloader(self, url):
    pass


if __name__ == "__main__":
    print("")
    print("****************")

    # 小说地址
    target_url = str(input("请输入小说目录下载地址"))

    # 实例化下载类
    d = download(target_url=target_url)
    name, numbers, url_dict = d.get_download_url();

    if name in os.listdir():
        os.remove(name)

    index = 1

    # 下载中
    print("《%s》 下载中: " % name[:-4])
    for key, value in url_dict.items():
        d.Writer(key, name, d.Downloader(value))
        sys.stdout.write("已下载:%.3f%%" % float(index / numbers) + '\r')
        sys.stdout.flush()
        index += 1
    print("《%s》 下载完成！" % name[:-4])
