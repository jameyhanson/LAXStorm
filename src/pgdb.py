'''
Created on Jan 19, 2017

@author: jamey

DESC:  psycopg2 PostgreSQL database connection class
'''

import psycopg2

class PgDb:
    def __init__(self, dbname, user, password, host, port): 
        self.conn = psycopg2.connect(
                    dbname=dbname,
                    user=user,
                    password=password,
                    port = port,
                    host=host) #added to avoid 'connections on Unix domain socket "/var/pgsql_socket/.s.PGSQL.5432"?'
        self.cur = self.conn.cursor()
        
    def exec_sql(self, sql):
        self.cur.execute(sql)
        self.conn.commit()
    
    def get_cursor(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()