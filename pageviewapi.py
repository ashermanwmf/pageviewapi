import os
import sys
import datetime
from collections import defaultdict
from mwviews.api import PageviewsClient

today = datetime.datetime.today() 

p = PageviewsClient()

# the first blank spot is reserved for the english version or 'original article page'. Added langauge codes after.
code = [ '', 'es' ]

for c in code:

	#what wiki is it on?
	w = sys.argv[1]

	#what is the article title?
	t = sys.argv[2]

	sd = '20150901'

	ed = today.strftime('%Y%m%d') 

	l = '/'

	if c == '':
		l = ''
	else:
		l = l + c

	views = p.article_views(w + '.wikimedia.org', [t + l], access='all-access', start=sd , end=ed )

	a = int()

	for key, value in views.iteritems():

		v = value.get(t)

		if isinstance(v, int) == True:
			a += v
		else:
			pass

	print t + '/' + c + ' ' + str(a)
