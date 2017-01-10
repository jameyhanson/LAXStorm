'''
Created on Jan 7, 2017

@author: jamey
'''
import psycopg2
from geopy import geocoders
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
    if geocoder == 'arcgis':
        geolocator = geocoders.ArcGIS()
    elif geocoder == 'baidu':
        geolocator = geocoders.baidu()
    elif geocoder == 'geocodefarm':
        print("Troubleshooting AttributeError: 'NoneType' object has no attribute 'replace'")
        exit(0)
        # geolocator = GeocodeFarm()
    elif geocoder == 'geocoderdotus':
        geolocator = geocoders.GeocoderDotUS()
    elif geocoder == 'geonames':
        geolocator = geocoders.geonames()
    elif geocoder == 'googlev3':
        geolocator = geocoders.GoogleV3()
    elif geocoder == 'nominatim':
        geolocator = geocoders.Nominatim()
    elif geocoder == 'openmapquest':
        geolocator = geocoders.OpenMapQuest()
    elif geocoder == 'yandex':
        print('Do not use.  Russian site')
        exit(1)
    else:
        print('invalid geodocder specified')
        exit(1)
        
    try:
        return geolocator.geocode(lookup_hs_name, exactly_one=True, timeout=10)
    except exc.GeocoderQuotaExceeded:
        print(geocoder, ':\tGeocoderQuotaExceeded')
        exit(1)
    except exc.ConfigurationError:
        print(geocoder, ':\tConfigurationError')
        exit(1)
    except exc.GeocoderAuthenticationFailure:
        print(geocoder, ':\tGeocoderAuthenticationFailure')
        exit(1)
    except exc.GeocoderTimedOut:
        print(geocoder, ':\tGeocoderTimedOut')
        exit(1)
    except exc.GeocoderUnavailable:
        print(geocoder, ':\tGeocoderUnavailable')
        exit(1)
    except exc.GeocoderInsufficientPrivileges:
        print(geocoder, ':\tGeocderInsufficientPrivileges')
    except:
        return None

def getHSList(curr, geocoder, num_schools):
    sql = '''
    SELECT
        id,
        searched_name,
        state,
        country
    FROM lax.high_schools
    WHERE geotried_''' + geocoder + ''' Is False
    AND geolocated Is False
    ORDER BY id DESC
    LIMIT ''' + str(num_schools) + ';'

    curr.execute(sql)
    return(curr.fetchall())

def runSQL(conn, sql):
    curr = conn.cursor()
    curr.execute(sql)
    conn.commit()

def main():
    num_schools = 50
    conn = getConnection()
    curr = conn.cursor()
    geocoder = 'nominatim'
    
    '''
    arcgis                      https://developers.arcgis.com/rest/geocode/api-reference/overview-world-geocoding-service.htm
    baidu            api_key    http://developer.baidu.com/map/webservice-geocoding.htm
    bing             api_key    https://msdn.microsoft.com/en-us/library/ff701715.aspx
    geocodefarm                 https://www.geocode.farm/geocoding/free-api-documentation/
    geocoderdotus               http://geocoder.us/
    geonames                    http://www.geonames.org/export/geonames-search.html
    googlev3                    https://developers.google.com/maps/documentation/geocoding/
    liveaddress      auth_token https://smartystreets.com/products/liveaddress-api
    navidata                    http://www.navidata.pl
    nominatim                   https://wiki.openstreetmap.org/wiki/Nominatim
    opencage         api_key    http://geocoder.opencagedata.com/api.html
    ERROR IN pygeo                openmapquest                http://developer.mapquest.com/web/products/open/geocoding-service
    yahooplacefinder consumer_key https://developer.yahoo.com/boss/geo/docs/
    whatthreewords   api_key    http://what3words.com/api/reference
    DO NO USE                     yandex                      http://api.yandex.com/maps/doc/geocoder/desc/concepts/input_params.xml'''
    
    HSList = getHSList(curr, geocoder, num_schools)
    
    num_geocoded = 0
    num_located = 0
    lookup_counter = 0
    
    for high_school in HSList:
        num_geocoded += 1
        id = high_school[0]
        # lax.high_schools.searched_name         .state                 .country
        lookup_hs_name = high_school[1] + ', ' + high_school[2] +', ' + high_school[3]
        location = geocodeHS(geocoder, id, lookup_hs_name)
        lookup_counter += 1
        if location == None:
             sql = 'UPDATE lax.high_schools SET geotried_' + geocoder + '=TRUE WHERE id=' + str(id) + ';'
             runSQL(conn, sql)
             print(str(lookup_counter) + ' of ' + str(num_schools) + 
                   '\tdid not find:\t', str(id), '\t', lookup_hs_name)
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
            print(str(lookup_counter) + ' of ' + str(num_schools) + 
                  '\tfound:\t\t', str(id), '\t', lookup_hs_name)
    print('\n' + str(num_geocoded) + ' schools looked up\t', str(num_located), ' geocoded')

    conn.close()
    
if __name__ == '__main__':
    main()