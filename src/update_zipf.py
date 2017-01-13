'''
Created on Jan 10, 2017

@author: jamey

Desc: update Zipf weight on rankings

'''
import psycopg2
from zipf import ZipfNorm

def getConnection():
    conn = psycopg2.connect(
                        dbname='lax',
                        user='lax',
                        port = 5432,
                        host='/tmp/', #added to avoid 'connections on Unix domain socket "/var/pgsql_socket/.s.PGSQL.5432"?'
                        password='cloudera')
    return conn

def runSQL(conn, sql):
    curr = conn.cursor()
    curr.execute(sql)
    conn.commit()

def main():
    # N = number of items in population
    # k = rank
    # s = Zipf coefficient.  > 1 is more left-skewed
    N = 1500
    k = 10
    s = 0.33
    
    conn = getConnection()
    curr = conn.cursor()
        
    for k in range(1, N + 1):
        z = ZipfNorm(N, k, s)
        
        sql = ('UPDATE lax.hs_ranks ' + 
               'SET zipf_weight = ' + str(z) +
               ' WHERE rank = ' + str(k) + ';')
        
        runSQL(conn, sql)
        print('Updated rank = ', k, ' with Zipf = ', '{0:.3f}'.format(z))
    conn.close()

if __name__ == '__main__':
    main()