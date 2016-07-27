__author__ = 'hzfanyaling'


from bs4 import BeautifulSoup
import urllib
import requests
import openpyxl
from openpyxl.reader.excel import load_workbook
from openpyxl.writer.excel import ExcelWriter
from openpyxl.workbook import Workbook
import titlecase
kabi = []
def game_spider():

		html_doc = 'https://www.douban.com/game/explore'
		content = requests.get(html_doc).content
		print(content)


def main():
	game_spider()


if __name__ == '__main__':
	main()