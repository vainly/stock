__author__ = 'chaclus'

import requests


url = "http://bbs.10jqka.com.cn/codelist.html"

rsp = requests.get(url)
rsp.encoding = 'gbk'
print rsp.text




