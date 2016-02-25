#########################################################################
# 	How this works								
# 1. This script accepts two arguments.							  		
# 2. Argument one is the wiki project <wiki.wiki(m/p)edia>.  			
# 3. Arguement two is the name of the article or page.		 			
# 4. turn graphing on by removing the # in front of drawgraph(graph).	
# ex: $ python pageviewapi.py commons.wikimedia File:Dog.png
#########################################################################

import os
import sys
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from collections import defaultdict
from mwviews.api import PageviewsClient

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

# the first blank spot is reserved for the english version or 'original article page'. Add langauge codes after.
code = [ '' ] 
# 'cs' , 'he' , 'da' , 'de' , 'eo' , 'el' , 'es' , 'fr' , 'id' , 'lb' , 'ro' , 'it' , 'ja' , 
# 		'lt' , 'ms' , 'mk' , 'mn' , 'no' , 'nan' , 'nb' , 'or' , 'ps' , 'pt' , 'pt-br' , 'pl' , 'sr' , 
# 		'sk' , 'sv' , 'pt-br' , 'ru' , 'ta' , 'th' , 'uk' , 'vi' , 'yi' , 'yue' , 'zh']

view_total = int()

dictionary = defaultdict(int)

t = ''

graph = []

for c in code:

	#what wiki is it on?
	w = sys.argv[1]

	#what is the article title?
	t = sys.argv[2]

	sd = '20150901'

	ed = today.strftime('%Y%m%d') 

	l = '/'

	l = checkempty(l ,c)

	try:

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