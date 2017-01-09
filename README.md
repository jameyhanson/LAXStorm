# LAXStorm
Lacrosse spreading across North America like a storm
**This project is intended to use the high school boys and girls lacrosse team rankings in LAXPower magazine, www.laxpower.com, to geocode the high schools display the results in a heat map over the last 10+ years**  

## Structure  
Python scripts, Google's geocoder, PostgreSQL for persistent storage and Boundless for heat-map display.  
I chose PostgreSQL because it supports JSON, which is returned by the geocoder, and GIS data types/operators.  

The planned sequence is:  
 1. pg_setup.py: create PostgreSQL tables
 2. get_lax_ranks.py to scrape the rank from www.laxpower.com.   Results are written to PostgreSQL and a .tsv  
 3. pg_normalize_hs.py: normalize the data in PostgreSQL so that high schools are in a consolidated table with a one-to-many relationship with the rank.  This prevents duplicate high school geocode look ups.
 4. hs_geocode.py: use Google to geocode high schools.  Note that this is an iterative process because some schools won't geocode  
 5. get_heatmap_data.py: extract the data into a format for heatmap display
 6. generate_heatmaps.py: generate the heat maps.  
 
## Prereqs and packags  
QGIS from http://www.kyngchaos.com/software/qgis  
This includes GDAL and Python libraries NumPy & matplotlib.  QGIS uses Python 2.7, but the rest of the code is Python 3.5.2.  I used `pip3` to install modules in Python 3.5.2 and the QGIS supplied .dmg files for Python 2.7.     
 
## ToDo
 7-Jan-16: Find out how to use GoogleV3 with geopy and code that as an option  
           see  https://developers.google.com/maps/documentation/geocoding/
