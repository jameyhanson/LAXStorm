'''
Created on Jan 6, 2017

@author: jamey

Desc: normalize the data in PostgreSQL so that high schools 
      are in a consolidated table with a one-to-many relationship with the hs_rank.
      This prevents duplicate high school geocode look ups
'''

import psycopg2

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
    conn = getConnection()
    
    # Prepare the database and schema
    sql = ('DROP SCHEMA IF EXISTS lax CASCADE;' )
    runSQL(conn, sql)
    print('Updated lax.high_schools')
    
    conn.close()
    
    print('SQL complete')

if __name__ == '__main__':
    main()