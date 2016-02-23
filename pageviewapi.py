import os
import sys
import datetime
from collections import defaultdict
from mwviews.api import PageviewsClient

p = PageviewsClient()

# the first blank spot is reserved for the english version or 'original article page'. Added langauge codes after.
code = [ '', 'cs']

for c in code:

	t = sys.argv[1]

	sd = sys.argv[2]

	ed = sys.argv[3]

	l = '%2f'

	if c == '':
		l = ''
	else:
		l = l + c

	try: 
		views = p.article_views('meta.wikimedia.org', [t + l], access='all-access', start=sd , end=ed )

		a = int()

		for key, value in views.iteritems():

			v = value.get(t)

			if isinstance(v, int) == True:
				a += v
			else:
				pass
	except Exception:
		a = 'N/A'

	print t + '/' + c + ' ' + str(a)
