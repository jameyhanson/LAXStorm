'''
Created on Jan 7, 2017

@author: jamey
'''
import psycopg2
from geopy.geocoders import Nominatim
from geopy import exc
from sys import exit


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
            return geolocator.geocode(lookup_hs_name, exactly_one=True)
        except exc.GeocoderQuotaExceeded:
            print(geocoder, ':/tGeocoderQuotaExceeded')
            exit(1)
        except exc.ConfigurationError:
            print(geocoder, ':/tConfigurationError')
            exit(1)
        except exc.GeocoderAuthenticationFailure:
            print(geocoder, ':/tGeocoderAuthenticationFailure')
            exit(1)
        except exc.GeocoderTimedOut:
            print(geocoder, ':/tGeocoderTimedOut')
            exit(1)
        except exc.GeocoderUnavailable:
            print(geocoder, ':/tGeocoderUnavailable')
            exit(1)
        except:
            return None

def getHSList(curr, geocoder, num_schools):
    sql = '''
    SELECT
        id,
        searched_name,
        state
    FROM lax.high_schools
    WHERE geotried_''' + geocoder + ''' Is False
    LIMIT ''' + str(num_schools) + ';'

    curr.execute(sql)
    return(curr.fetchall())

def runSQL(conn, sql):
    curr = conn.cursor()
    curr.execute(sql)
    conn.commit()

def main():
    num_schools = 200
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
    
    HSList = getHSList(curr, geocoder, num_schools)
    
    num_geocoded = 0
    num_located = 0
    
    for high_school in HSList:
        num_geocoded += 1
        id = high_school[0]
        lookup_hs_name = high_school[1] + ', ' + high_school[2]
        location = geocodeHS(geocoder, id, lookup_hs_name)
        print('lookup up:\t' + str(id) + '\t' + lookup_hs_name)
        # update geotried_<geocoder> = True
        # if != None, update latitude, longitude, address, and JSON
        if location == None:
             sql = 'UPDATE lax.high_schools SET geotried_' + geocoder + '=TRUE WHERE id=' + str(id) + ';'
             runSQL(conn, sql)
        else:
            sql = ("UPDATE lax.high_schools SET geotried_" + geocoder + "=TRUE, " +
                  "geolocated = TRUE, " + 
                  "latitude = " + str(location.latitude) + ", " +
                  "longitude = " + str(location.longitude) + ", " +
                  "address = '" + location.address.replace("'", "''") + "', " +
                  "json_response = '" + str(location.raw).replace("'", "''") + 
                  "' WHERE id=" + str(id) + ";")
            runSQL(conn, sql)
            num_located += 1
    print(str(num_geocoded) + ' hs looked up\t', str(num_located), ' geocoded')

    conn.close()
    
if __name__ == '__main__':
    main()