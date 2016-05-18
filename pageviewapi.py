#########################################################################
# 	How this works								
# 1. This script accepts two arguments.							  		
# 2. Argument one is the wiki project <wiki.wiki(m/p)edia>.  			
# 3. Arguement two is the name of the article or page.		 			
# 4. turn graphing on by removing the # in front of drawgraph(graph).	
# ex: $ python pageviewapi.py commons.wikimedia File:Dog.png
# (two packages: mwviews and matplotlib)
#########################################################################

import os
import sys
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from collections import defaultdict
from mwviews.api import PageviewsClient


# add l = '' for wikipedia pageview per lanugage version

# add subpage extension to article title.
def checkempty(l, c):
	if c == '':
		l = ''
	else:
		l = l + c

	return l 

# create a list of integers to be drawn into line by drawgraph()
def graphlist(data):
	for d in data:
		if views[d].values() == [None]:
			graph.append(0)
		else:
			f = views[d].values()
			graph.append(f[0])

# creates a graph for each page that runs through the loop of adding langauge codes.
def drawgraph(data):
	plt.plot(data)
	plt.xlabel('Date')
	plt.ylabel('Views')
	plt.title(t + l)
	plt.show()

# add up the total views for a sub page
def addtotalviews(data, a):
	for key, value in data.iteritems():

		v = value.get(t + l)

		if isinstance(v, int) == True:
			a += v
		else:
			pass

	return a

today = datetime.datetime.today() 

p = PageviewsClient()

# the first blank spot is reserved for the english (unless modified for wikipedia language versions, then add 'en' first) 
#	version or 'original article page'. Add langauge codes after.
code = [ '' ]

#add to code array for all language versions of a page
# , 'es' , 'aa' , 'ab' , 'ae' , 'af' , 'ak' , 'am' , 'an' , 'ar' , 'as' , 
# 'av' , 'ay' , 'az' , 'ba' , 'be' , 'bg' , 'bh' , 'bi' , 'bm' , 'bn' , 'bo' , 
# 'br' , 'bs' , 'ca' , 'ce' , 'ch' , 'co' , 'cr' , 'cs' , 'cu' , 'cv' , 'cy' , 
# 'da' , 'de' , 'dv' , 'dz' , 'ee' , 'el' , 'eo' , 'es' , 'et' , 'eu' , 'fa' , 
# 'ff' , 'fi' , 'fj' , 'fo' , 'fr' , 'fy' , 'ga' , 'gd' , 'gl' , 'gn' , 'gu' , 
# 'gv' , 'ha' , 'he' , 'hi' , 'ho' , 'hr' , 'ht' , 'hu' , 'hy' , 'hz' , 'ia' , 
# 'id' , 'ie' , 'ig' , 'ii' , 'ik' , 'io' , 'is' , 'it' , 'iu' , 'ja' , 'jv' , 
# 'ka' , 'kg' , 'ki' , 'kj' , 'kk' , 'kl' , 'km' , 'kn' , 'ko' , 'kr' , 'ks' , 
# 'ku' , 'kv' , 'kw' , 'ky' , 'la' , 'lb' , 'lg' , 'li' , 'ln' , 'lo' , 'lt' , 
# 'lu' , 'lv' , 'mg' , 'mh' , 'mi' , 'mk' , 'ml' , 'mn' , 'mr' , 'ms' , 'mt' , 
# 'my' , 'na' , 'nb' , 'nd' , 'ne' , 'ng' , 'nl' , 'nn' , 'no' , 'nr' , 'nv' , 
# 'ny' , 'oc' , 'oj' , 'om' , 'or' , 'os' , 'pa' , 'pi' , 'pl' , 'ps' , 'pt' , 
# 'qu' , 'rm' , 'rn' , 'ro' , 'ru' , 'rw' , 'sa' , 'sc' , 'sd' , 'se' , 'sg' , 
# 'si' , 'sk' , 'sl' , 'sm' , 'sn' , 'so' , 'sq' , 'sr' , 'ss' , 'st' , 'su' , 
# 'sv' , 'sw' , 'ta' , 'te' , 'tg' , 'th' , 'ti' , 'tk' , 'tl' , 'tn' , 'to' , 
# 'tr' , 'ts' , 'tt' , 'tw' , 'ty' , 'ug' , 'uk' , 'ur' , 'uz' , 've' , 'vi' , 
# 'vo' , 'wa' , 'wo' , 'xh' , 'yi' , 'yo' , 'za' , 'zh' , 'zu' ] 

view_total = int()

dictionary = defaultdict(int)

t = ''

graph = []

sys.tracebacklimit = 0

for c in code:

	#what wiki is it on? Add c + '.' + for wikipedia page views per language version
	w = sys.argv[1]

	#what is the article title?
	t = sys.argv[2]

	# 20150901 is start of tool
	sd = '20150901'

	ed = today.strftime('%Y%m%d') 

	# remove for wikipedia views per language version
	l = '/'

	# remove for wikipedia views per language version
	l = checkempty(l ,c)

	try:

		# remove +l for wikipedia views per language version 
		views = p.article_views(w, [t + l], access='all-access', start=sd , end=ed)

		dates = sorted(views.keys())
		
		graphlist(dates)

		a = int()

		# add up all supage views
		view_total += addtotalviews(views, a)

	except Exception: 

		a = 0
		pass

	# dictionary of subpage total page views
	dict_add = {str(t + '/' + c): { "Views" : str(addtotalviews(views, a)) }}

	dictionary.update(dict_add)

	#drawgraph(graph)
	
# print each subpage and its total page views from dictionary of subpage total page views.
for key, value in dictionary.iteritems():
	print key + ' = ' + value.get('Views')

# print the total views of all supages for article.
print t + ' TOTAL_VIEWS = ' + str(view_total)