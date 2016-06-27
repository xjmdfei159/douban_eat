#!/usr/bin/env python
# encoding: utf-8

__author__ = 'hzfanyaling'

localPath = 'D:\kabi'

import re
import urllib

import os

imagepic = 0
def get_html(html):
	page = urllib.urlopen(html)
	html = page.read()
	return html

def get_img(html):
	reg = r'<img width="170" src="(.+?\.jpg)" alt='
	des = r'<h1>.+?\</h1>'
	like = r'<span class="fav-num">.+?\<'
	#print(des)
	imgre= re.compile(reg)
	imglist= re.findall(imgre,html)
	tegre = re.compile(des)
	teglist = re.findall(tegre,html)
	ligre = re.compile(like)
	lilist = re.findall(ligre,html)
	print(lilist)
	print(teglist[0])

	#return imglist
	picpath = 'D:\patupian'
	if not os.path.exists(picpath):
		os.makedirs(picpath)
	x = 0
	for imgurl in imglist:
		target = picpath + '\\%s.jpg' % x
		#target = picpath + '\' + teglist[0]
		print ('Downloading image1 to location: ' + target + '\nurl=' + imgurl)
		global imagepic
		imagepic = urllib.urlretrieve(imgurl, target)
		x += 1
	return imagepic

def main():
	html = get_html("https://www.douban.com/subject/10734163/")


	print (get_img(html))
if __name__ == "__main__":
	main()