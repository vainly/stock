__author__ = 'chaclus'

import requests


url = "http://market.finance.sina.com.cn/downxls.php?date=2015-07-08&symbol=sh600021"

rsp = requests.get(url)
# rsp.encoding =

# print " rsp status_code : %s , content_length : %s " % (rsp.status_code, rsp.headers['content-length'])
print " rsp status_code : %s , content_length : %s " % (rsp.status_code, rsp.headers.get('Content-Disposition'))

file_name = '/Users/chaclus/Workspace/PycharmProjects/stock/files/sh600021_2016-07-08.csv'
chunk_size = 1024
if rsp.status_code == requests.codes.ok:
    with open(file_name, "wb") as fn:
        for chunk in rsp.iter_content(chunk_size):
            fn.write(chunk)
