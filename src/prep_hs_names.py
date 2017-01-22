'''
Created on Jan 6, 2017

@author: jamey
Desc: create PostgreSQL tables for LAXStorm persistent storage and analysis
'''
from pgdb import PgDb

def main():
    SCHEMA = 'lam' # Use 'lax' for production
    pgdb = PgDb(dbname='lax', user='lax', password='cloudera', host='/tmp/', port=5432)
    
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
    UPDATE ''' + SCHEMA + '''.high_schools
    SET script_updated_name = REPLACE(raw_name, ' HS', ' High School')
    WHERE raw_name LIKE '% HS';
    '''
    pgdb.exec_sql(sql)
    print('HS to High School replacement made')
    
    sql = '''
    UPDATE ''' + SCHEMA + '''.high_schools
    SET script_updated_name = REPLACE(raw_name, ' Sch', ' School')
    WHERE raw_name LIKE '% Sch';
    '''
    pgdb.exec_sql(sql)
    print('Sch to School replacement made')
    
    sql = '''
    UPDATE ''' + SCHEMA + '''.high_schools
    SET script_updated_name = REPLACE(raw_name, ' CDS', ' Country Day School')
    WHERE raw_name LIKE '% CDS';
    '''
    pgdb.exec_sql(sql)
    print('CDS to Country Day School replacement made')
    
    sql = '''
    UPDATE ''' + SCHEMA + '''.high_schools
    SET script_updated_name = raw_name || ' High School'
    WHERE raw_name NOT LIKE '%School%'
    AND raw_name NOT LIKE '% CS'
    AND script_updated_name IS NULL;
    '''
    pgdb.exec_sql(sql)
    print('appended High School to names not containing School made')
    
    sql = '''
    UPDATE ''' + SCHEMA + '''.high_schools
    SET searched_name = COALESCE(script_updated_name, raw_name);
    '''
    pgdb.exec_sql(sql)
    print('populated searched_name field')

    sql = '''
    UPDATE ''' + SCHEMA + '''.high_schools
    SET country = 'Canada'
    WHERE state in ('AB', 'BC', 'MB', 'NB', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT');
    '''
    pgdb.exec_sql(sql)
    print('updated Canadian schools')
    
    sql = '''
    UPDATE ''' + SCHEMA + '''.high_schools
    SET country = 'United States of America'
    WHERE country IS NULL;
    '''
    pgdb.exec_sql(sql)
    print('updated USA schools')        
    
    print('prep_hs_names.py complete')
    
if __name__ == '__main__':
    main()