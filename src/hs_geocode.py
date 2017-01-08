'''
Created on Jan 7, 2017

@author: jamey
'''
import psycopg2
import geopy
from sys import exit
from geopy.geocoders import Nominatim

def getConnection():
    conn = psycopg2.connect(
                        dbname='lax',
                        user='lax',
                        port = 5432,
                        host='/tmp/', #added to avoid 'connections on Unix domain socket "/var/pgsql_socket/.s.PGSQL.5432"?'
                        password='cloudera')
    return conn

def geocodeHS(geocoder, id, lookup_hs_name):
    if geocoder == 'nominatim':
        geolocator = Nominatim()
        try:
            return geolocator.geocode(lookup_hs_name)
        except:
            return None

def getHSList(curr, geocoder):
    sql = '''
    SELECT
        id,
        searched_name,
        state
    FROM lax.high_schools
    WHERE geotried_''' + geocoder + ''' Is False
    LIMIT 3;'''

    curr.execute(sql)
    return(curr.fetchall())

def main():
    conn = getConnection()
    curr = conn.cursor()
    geocoder = 'nominatim'
    '''
    arcgis
    baidu
    bing
    databc
    geocodefarm
    geonames
    googlev3
    liveaddress
    navidata
    nominatim
    opencage
    openmapquest
    yahooplacefinder
    whatthreewords
    yandex'''
    
    HSList = getHSList(curr, geocoder)
    
    for high_school in HSList:
        id = high_school[0]
        lookup_hs_name = high_school[1] + ', ' + high_school[2]
        location = geocodeHS(geocoder, id, lookup_hs_name)
        
        # update geotried_<geocoder> = True
        # if != None, update latitude, longitude, address, and json_response
        if location == None:
            print(str(id), lookup_hs_name, '\t returned: None')
        else:
            print(str(id), lookup_hs_name, '\t returned: ', location.latitude, location.longitude, location.address)

    conn.close()
    
if __name__ == '__main__':
    main()