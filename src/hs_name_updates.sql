-- Testing hs name changes to improve geocoding
SELECT COUNT(*), ROUND(COUNT(*)/4878.0*100,2) AS percent FROM lax.high_schools WHERE geolocated = True;

SELECT 
  id,
  raw_name,
  searched_name,
  state,
  country
FROM lax.high_schools
WHERE geolocated IS FALSE
ORDER BY id DESC;

-- testing query
SELECT 
  id,
  raw_name, 
  searched_name,
  state,
  country,
  geolocated
FROM lax.high_schools
WHERE raw_name LIKE 'Acad %'
AND geolocated = False
ORDER BY id;

-- Remove 'High School' if contains 'LC' and replace with 'Lacrosse Club'
UPDATE lax.high_schools
SET searched_name = REPLACE(raw_name, 'LC', 'Lacrosse Club'),
  geotried_googlev3 = False,
  geotried_nominatim = False
WHERE geolocated = False
AND raw_name LIKE '%LC';

-- Remove 'High School' if contains 'Acad' and add 'emy'
UPDATE lax.high_schools
SET searched_name = raw_name || 'emy',
  geotried_googlev3 = False,
  geotried_nominatim = False
WHERE geolocated = False
AND raw_name LIKE '%Acad';

-- Remove 'High School' if contains 'Charter'
UPDATE lax.high_schools
SET searched_name = raw_name,
  geotried_googlev3 = False,
  geotried_nominatim = False
WHERE geolocated = False
AND raw_name LIKE '%Charter%';

-- Remove 'High School' if contains 'Prep'
UPDATE lax.high_schools
SET searched_name = raw_name,
  geotried_googlev3 = False,
  geotried_nominatim = False
WHERE geolocated = False
AND raw_name LIKE '%Prep%';

-- Remove 'High School' if contains 'Day'
UPDATE lax.high_schools
SET searched_name = raw_name,
  geotried_googlev3 = False,
  geotried_nominatim = False
WHERE geolocated = False
AND raw_name LIKE '%Day%';

-- Remove 'High School' if contains 'Club'
UPDATE lax.high_schools
SET searched_name = raw_name,
  geotried_googlev3 = False,
  geotried_nominatim = False
WHERE geolocated = False
AND raw_name LIKE '%Club%';

-- Remove 'High School' if contains 'Academy'
UPDATE lax.high_schools
SET searched_name = raw_name,
  geotried_googlev3 = False,
  geotried_nominatim = False
WHERE geolocated = False
AND raw_name LIKE '%Academy%';


-- Remove 'High School' if contains 'Institute'
UPDATE lax.high_schools
SET searched_name = raw_name,
  geotried_googlev3 = False,
  geotried_nominatim = False
WHERE geolocated = False
AND raw_name LIKE '%Institute%';