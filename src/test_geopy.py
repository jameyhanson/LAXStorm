'''
Created on Jan 7, 2017

@author: jamey

test: John Carroll CS, FL
'''

from geopy import geocoders

def main():
    search_string = 'Poly Prep Country Day School, NY'
    
    geolocator = geocoders.GeoNames()
    location = geolocator.geocode(search_string)
    
    if location == None:
        print('None found')
    else:
        print(location.address)

if __name__ == '__main__':
    main()