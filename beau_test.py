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
	html_doc = "https://www.douban.com/subject/all?cat_id=1000"
	page = urllib.urlopen(html_doc)
	#html = page.read()
	soup = BeautifulSoup(page,'html.parser')
	test = soup.findAll('div',{'class':"pic"})
	for i in range(0,len(test)):
		test_title = test[i].a['title']
		test_web = test[i].a['href']
		test_pic = test[i].img['src']
		print(test_title + ' web:' + test_web +	' pic:' + test_pic)



if __name__ == '__main__':
	main()