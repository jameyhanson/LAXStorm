'''
Created on Jan 10, 2017

@author: jamey

Desc: update Zipf weight on rankings

'''
from zipf import ZipfNorm

from pgdb import PgDb

def main():
    # N = number of items in population
    # k = rank
    # s = Zipf coefficient.  > 1 is more left-skewed
    N = 1500
    k = 10
    s = 0.33
    
    SCHEMA = 'lam' # Use 'lax' for production
    pgdb = PgDb(dbname='lax', user='lax', password='cloudera', host='/tmp/', port=5432)
        
    for k in range(1, N + 1):
        z = ZipfNorm(N, k, s)
        
        sql = ('UPDATE ' + SCHEMA + '.hs_ranks ' + 
               'SET zipf_weight = ' + str(z) +
               ' WHERE rank = ' + str(k) + ';')
        
        pgdb.exec_sql(sql)
        print('Updated rank = ', k, ' with Zipf = ', '{0:.3f}'.format(z))

if __name__ == '__main__':
    main()