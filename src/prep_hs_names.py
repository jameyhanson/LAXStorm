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
    
    '''
    Scripted high school name replacements:
    
    HS    High School 
    Sch   School
    CDS   Country Day School
    
    Did not script these possible replacements:
    CS    Country School
          Christian School
          Catholic School
    '''
    
    sql = '''
    UPDATE lax.high_schools
    SET script_updated_name = REPLACE(raw_name, ' HS', ' High School')
    WHERE raw_name LIKE '% HS';
    '''
    runSQL(conn, sql)
    print('HS to High School replacement made')
    
    sql = '''
    UPDATE lax.high_schools
    SET script_updated_name = REPLACE(raw_name, ' Sch', ' School')
    WHERE raw_name LIKE '% Sch';
    '''
    runSQL(conn, sql)
    print('Sch to School replacement made')
    
    sql = '''
    UPDATE lax.high_schools
    SET script_updated_name = REPLACE(raw_name, ' CDS', ' Country Day School')
    WHERE raw_name LIKE '% CDS';
    '''
    runSQL(conn, sql)
    print('CDS to Country Day School replacement made')
    
    sql = '''
    UPDATE lax.high_schools
    SET script_updated_name = raw_name || ' High School'
    WHERE raw_name NOT LIKE '%School%'
    AND raw_name NOT LIKE '% CS'
    AND script_updated_name IS NULL;
    '''
    runSQL(conn, sql)
    print('appended High School to names not containing School made')
    
    sql = '''
    UPDATE lax.high_schools
    SET searched_name = COALESCE(script_updated_name, raw_name);
    '''
    runSQL(conn, sql)
    print('populated searched_name field')
    
    conn.close()
    
    print('prep_hs_names.py complete')
    
if __name__ == '__main__':
    main()