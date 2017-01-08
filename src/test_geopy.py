'''
Created on Jan 7, 2017

@author: jamey

test: John Carroll CS, FL
'''

from geopy.geocoders import Nominatim

def main():
    geolocator = Nominatim()
    string = 'Hilton Head High School, SC'
    location = geolocator.geocode(string)
    #location = geolocator("Poly Prep Country Day School, NY")
    if location == None:
        print('None found')
    else:
        print(location.address)

if __name__ == '__main__':
    main()