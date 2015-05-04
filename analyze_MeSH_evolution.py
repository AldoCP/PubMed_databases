#!/usr/bin/python
# -*- coding: utf-8 -*-


import MySQLdb as mdb
#import sys
import pandas as pd
import numpy as np
import matplotlib
#matplotlib.style.use('ggplot')
pd.options.display.mpl_style = 'default'


try:
	con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')

	sql="SELECT * FROM(SELECT YEAR(x.Dates) AS Years, x.MeSH, count(x.MeSH) AS countss, y.totals FROM MeSHRec AS x LEFT JOIN (SELECT MeSH, count(MeSH) AS totals FROM MeSHRec GROUP BY 1) AS y ON x.MeSH = y.MeSH GROUP BY 1, 2) AS z WHERE totals>=2000 ORDER BY Years DESC, totals DESC"
	df = pd.read_sql(sql, con)
	df['normalized'] = df.countss/df.totals
	df.groupby('MeSH').apply(len) # Some descriptive frequencies
	def scales(x):
		return pd.DataFrame({
		'Years': x['Years'],
		'MeSH': x['MeSH'],
		'scaled':(x['countss']-np.mean(x['countss']))/np.std(x['countss'])})#
	df2 = df.groupby('MeSH').apply(scales)
	df2.to_csv('forPlotly.csv')

except mdb.Error, e:
  
    if con:
        con.rollback()
        
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:    
            
    if con:    
        con.close()


