#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import numpy as np
from Bio import Medline
from Bio import Entrez
from joblib import Parallel, delayed
import multiprocessing
Entrez.email = "someone@x.x"


num_cores = multiprocessing.cpu_count()

try:
	con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')

	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS MeSH002")
	cur.execute("CREATE TABLE MeSH002(Id INT PRIMARY KEY AUTO_INCREMENT, \
		PMID INT, MeSH VARCHAR(50), Dates DATE) ENGINE=INNODB")
	query1 = '((psychology[MeSH]) AND ("2000/01/01"[Date - MeSH] : "2010/12/31"[Date - MeSH])) AND English[Language] '
	handle = Entrez.esearch(db="PubMed", retmax=25000, term=query1)
	record1 = Entrez.read(handle)["IdList"]
	handle.close()
	def processInput(k):
		print "Querying PMID: "+str(k)+"."
		getall = Medline.read(Entrez.efetch(db="pubmed", id=k, rettype="medline", retmode="text"))
		singlemesh = getall.get("MH")
		singledate = getall.get("EDAT")	
		for j1 in range(len(singlemesh)):
			cur.execute("INSERT INTO MeSH002(PMID, MeSH, Dates) VALUES("+str(k)+",'" + getall.get("MH")[j1][0:24].translate(None, "'*&")+"','" +  str(singledate[0:10]) +"')" )
	try:
		Parallel(n_jobs=num_cores)(delayed(processInput)(i) for i in record1)
	except:
		pass
	cur.execute("UPDATE MeSH002 SET MeSH = LEFT(MeSH, LOCATE('/',MeSH)-1) WHERE LOCATE('/',MeSH)>0")
	con.commit()
    
except mdb.Error, e:
  
    if con:
        con.rollback()
        
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:    
            
    if con:    
        con.close()


