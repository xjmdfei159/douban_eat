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
	html_doc = "https://www.douban.com/group/"
	page = urllib.urlopen(html_doc)
	#html = page.read()
	soup = BeautifulSoup(page,'html.parser')
	print(soup.title)


if __name__ == '__main__':
	main()