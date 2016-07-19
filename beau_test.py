#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: kabi
@license: Apache Licence 
@file: beau_test.py
@time: 2016/7/1 0001 上午 12:13
"""

from bs4 import BeautifulSoup
import urllib

def main():
	for i in range(0,30):
		html_doc = 'https://www.douban.com/subject/all?cat_id=1000&start=' + str(20*i)
		page = urllib.urlopen(html_doc)
		#html = page.read()
		soup = BeautifulSoup(page,'html.parser')
		test = soup.findAll('li',{'class':"thing-item"})
		test_li = soup.findAll('span',{'class':"favs"})
		print(len(test))
		for i in range(0,len(test)):
			test_title = test[i].a['title']
			test_web = test[i].a['href']
			test_pic = test[i].img['src']
			test_like = test_li[i].get_text()
			print(test_title + ' web:' + test_web +	' pic:' + test_pic + ' like:' +test_like)


if __name__ == '__main__':
	main()