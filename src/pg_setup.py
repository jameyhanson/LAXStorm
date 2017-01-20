'''
Created on Jan 6, 2017

@author: jamey
Desc: create PostgreSQL tables for LAXStorm persistent storage and analysis
'''
from pgdb import PgDb

def main():
    SCHEMA = 'lam' #Change to lax for production
    
    pgdb = PgDb(dbname='lax', user='lax', password='cloudera', host='/tmp/', port=5432)
    
    # Prepare the database and schema
    sql = ('DROP SCHEMA IF EXISTS ' + SCHEMA + ' CASCADE;' )
    pgdb.exec_sql(sql)
    
    sql = 'CREATE SCHEMA ' + SCHEMA + ';'
    pgdb.exec_sql(sql)
    
    # create tables
    sql= ('CREATE TABLE ' + SCHEMA + '.high_schools (' +
        '''
        id             SERIAL PRIMARY KEY,
        created_on     TIMESTAMP DEFAULT now(),
        raw_name       TEXT,
        state          TEXT,
        country        TEXT,
        script_updated_name TEXT,
        manually_updated_name TEXT,
        searched_name  TEXT,
        geo_code_name  TEXT,
        json_response  TEXT,
        json           JSONB,
        address        TEXT,
        latitude       NUMERIC,
        longitude      NUMERIC,
        geo_loc        GEOMETRY,
        geo_accuracy   TEXT,
        geotried_arcgis BOOLEAN DEFAULT FALSE,
        geotried_baidu BOOLEAN DEFAULT FALSE,
        geotried_bing  BOOLEAN DEFAULT FALSE,
        geotried_databc BOOLEAN DEFAULT FALSE,
        geotried_geocodefarm BOOLEAN DEFAULT FALSE,
        geotried_geocoderdotus BOOLEAN DEFAULT FALSE,
        geotried_geonames BOOLEAN DEFAULT FALSE,
        geotried_googlev3 BOOLEAN DEFAULT FALSE,
        geotried_liveaddress BOOLEAN DEFAULT FALSE,
        geotried_navidata BOOLEAN DEFAULT FALSE,
        geotried_nominatim BOOLEAN DEFAULT FALSE,
        geotried_opencage BOOLEAN DEFAULT FALSE,
        geotried_openmapquest BOOLEAN DEFAULT FALSE,
        geotried_yahooplacefinder BOOLEAN DEFAULT FALSE,
        geotried_whatthreewords BOOLEAN DEFAULT FALSE,
        geotried_yandex BOOLEAN DEFAULT FALSE,
        geolocated     BOOLEAN DEFAULT FALSE);''')
    pgdb.exec_sql(sql)
    
    print(SCHEMA + '.high_shools created')
    
    sql = ('CREATE TABLE ' + SCHEMA + '.hs_ranks (' + 
        'id             SERIAL PRIMARY KEY,' + 
        'hs_id          BIGINT REFERENCES ' + SCHEMA + '.high_schools (id),' +
        'created_on     TIMESTAMP DEFAULT now(),' +
        'url            TEXT,' + 
        'gender         CHAR(3),' +
        'year           NUMERIC,' +
        'rank           NUMERIC,' +
        'zipf_weight    NUMERIC,' +
        'raw_hs_name    TEXT,' +
        'state          CHAR(2));')
    pgdb.exec_sql(sql)
    
    print(SCHEMA + '.hs_ranks created')
    
if __name__ == '__main__':
    main()