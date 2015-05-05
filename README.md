# PubMed_databases

This code is mainly based on three Python modules: MySQLdb, Bio and pandas. 

"PubMed_databases" performs two main functions: 


## Extraction of keywords from PubMed articles 

The Medical Subject Heading (MeSH) terms are extracted from all the articles retrieved as "search results" from PubMed. 
This function is performed by the file "MeSH_to_MySQL.py". 
The MeSH terms are stored in a MySQL database with four columns: "Id", "PMID", "MeSH" and "Dates". 

+----+---------+------------+------------+

| Id  | PMID    | MeSH    | Dates |

+----+---------+------------+------------+

| 1 | 7701056 | Adult   | 1994-12-01  |

| 2 | 7701056 | Calcitriol  | 1994-12-01  |

| 3 | 7701056 | Female    | 1994-12-01  |

| 4 | 7701056 | Humans    | 1994-12-01  |

| 5 | 7701056 | Male    | 1994-12-01  |

+----+---------+------------+------------+

By default, this file assesses the whole literature on "Psychology" found in PubMed from 2000 to 2010 (~25000 articles). 

## Query of keywords from PubMed articles 

The databases created by "MeSH_to_MySQL.py" can be queried by "analyze_MeSH_evolution.py". 
The latter file evaluates the temporal evolution of the most popular terms in a database of MeSH terms, to show how the most popular MeSH terms in the query have changed over the years. 
As an example query, this file retrieves information from a MySQL database on all MeSH terms appearing in the literature >2000 times. 
For the case of the above PubMed query (articles about "Psychology" from 2000 to 2010), "analyze_MeSH_evolution.py" gets information on 12 highly popular MeSH terms, and writes their frequencies over the years to a text file entitled 'forPlotly.csv', which can be used for data visualization purposes. 

As an example, the image in the link https://plot.ly/~aldocp/99 shows the prominence of the 11 most popular MeSH terms related to "Psychology", from 2005 to 2010. 
As depicted, all these terms had a popularity peak by 2007, though their relative importance is decreasing with the years. This decrease is due to the appearance of new MeSH terms in recent years. Other important trend can be seen in the plot: the terms "Questionnaires", "United States" and "Adult" have rapidly lost popularity from 2009 to 2010 (more than expected by the overall trend). 
