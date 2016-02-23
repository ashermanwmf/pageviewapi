import os
import sys
import datetime
from collections import defaultdict
from mwviews.api import PageviewsClient

p = PageviewsClient()

t = sys.argv[1]

sd = sys.argv[2]

ed = sys.argv[3]

views = p.article_views('meta.wikimedia.org', [t], access='all-access', start=sd , end= ed )

a = int()

for key, value in views.iteritems():

	v = value.get(t)

	if isinstance(v, int) == True:
		a += v
	else:
		pass

print t + ' ' + str(a)
