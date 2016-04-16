#!/usr/bin/python

import requests
from bs4 import BeautifulSoup

def scrape(url):
	r = requests.get(url)
	bt = BeautifulSoup(r.content)
	hd1 = '<html>'
	hd2 = '<body style="background:black;"><center>'
	foot = '<a href="http://mangacanblog.com">Powered by Mangacan</a></center></body></html>'
	judul = bt.title
	j1 = str(judul).replace('|Baca Manga Komik Indonesia|Mangacan','')
	fix = bt.findAll('img')
	if 0 < 1:
		print hd1 + j1 + hd2
		for src1 in fix:
			print '<img src="' + src1.get("src") + '" width="990"/><hr color="red">'
		print foot
		
scrape('http://www.mangacanblog.com/baca-komik-shokugeki_no_soma-156.5-157.5-bahasa-indonesia-shokugeki_no_soma-156.5-terbaru.html')
