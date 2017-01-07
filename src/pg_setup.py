'''
Created on Jan 6, 2017

@author: jamey
Desc: create PostgreSQL tables for LAXStorm persistent storage and analysis
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
    
    sql = 'CREATE SCHEMA lax;'
    runSQL(conn, sql)
    
    # create tables
    sql='''
CREATE TABLE lax.high_schools (
    id             SERIAL PRIMARY KEY,
    created_on     TIMESTAMP DEFAULT now(),
    raw_name       TEXT,
    state          CHAR(2),
    script_updated_name TEXT,
    manually_updated_name TEXT,
    searched_name  TEXT,
    geo_code_name  TEXT,
    geolocate      JSONB,
    latitude       NUMERIC,
    longitude      NUMERIC,
    geo_accuracy   TEXT,
    geolocate_tried BOOLEAN,
    geolocated     BOOLEAN);'''
    runSQL(conn, sql)
    print('lax.high_shools created')
    
    sql = '''
CREATE TABLE lax.hs_ranks (
    id             SERIAL PRIMARY KEY,
    hs_id          BIGINT REFERENCES lax.high_schools (id),
    created_on     TIMESTAMP DEFAULT now(),
    url            TEXT,
    gender         CHAR(3),
    year           NUMERIC,
    rank           NUMERIC,
    zipf_weight    NUMERIC,
    raw_hs_name    TEXT,
    state          CHAR(2));'''
    runSQL(conn, sql)
    print('lax.hs_ranks created')

    conn.close()
    
    print('SQL complete')
    
if __name__ == '__main__':
    main()