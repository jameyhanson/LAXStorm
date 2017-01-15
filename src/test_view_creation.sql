-- Find top-20 high schools that have not been geolocated
-- 22 schools in the top 25 that were not automatically geocoded
SELECT *
FROM lax.high_schools
WHERE geolocated = False 
AND id IN (
    SELECT DISTINCT hs_id
    FROM lax.hs_ranks
    WHERE rank <= 100)
 ORDER BY id;

-- Manually geocode themUPDATE lax.high_schools
UPDATE lax.high_schools
SET searched_name = '500 Chestnut Ave, Towson',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 4641;

UPDATE lax.high_schools
SET searched_name = '1801 N Broom St, Wilmington',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 4615;

UPDATE lax.high_schools
SET searched_name = '3131 Stone Valley Rd, Danville',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 4292;

UPDATE lax.high_schools
SET searched_name = '418 S Warren Ave, Malvern',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 4286;

UPDATE lax.high_schools
SET searched_name = '1000 St Stephens Rd, Alexandria',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 4126;

UPDATE lax.high_schools
SET searched_name = '815 Hampton Ln, Towson',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 3952;

UPDATE lax.high_schools
SET searched_name = '5204 Roland Avenue, Baltimore',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 3841;

UPDATE lax.high_schools
SET searched_name = '1100 Shiloh Rd, West Chester',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 3641;

UPDATE lax.high_schools
SET searched_name = '1300 Academy Rd, Culver',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 2729;

UPDATE lax.high_schools
SET searched_name = '8605 W Cheltenham Ave, Glenside',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 2632;

UPDATE lax.high_schools
SET searched_name = '703 Churchville Rd, Bel Air',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 2007;

UPDATE lax.high_schools
SET searched_name = '1499 Hard Rd, Columbus',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 1604;

UPDATE lax.high_schools
SET searched_name = '875 Ridge Rd, Webster',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 960;

UPDATE lax.high_schools
SET searched_name = '8080 New Cut Rd, Severn',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 899;

UPDATE lax.high_schools
SET searched_name = '2001 37th Ave, San Francisco',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 848;

UPDATE lax.high_schools
SET searched_name = '60 N Salem Rd, Cross River',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 816;

UPDATE lax.high_schools
SET searched_name = '1000 St Stephens Rd, Alexandria',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 787;

UPDATE lax.high_schools
SET searched_name = '5204 Roland Avenue, Baltimore',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 643;

UPDATE lax.high_schools
SET searched_name = '113 Duke of Gloucester St, Annapolis',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 603;

UPDATE lax.high_schools
SET searched_name = '2600 Rutherford Rd, Concord',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 257;

UPDATE lax.high_schools
SET searched_name = '10900 Rockville Pike, North Bethesda',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 209;

UPDATE lax.high_schools
SET searched_name = '1524 35th St NW',
state = 'DC',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 3117;


-- test weighted output
SELECT
  hr.rank,
  hs.raw_name,
  hs.state, 
  hs.latitude,
  hs.longitude,
  -- hr.rank,
  hr.zipf_weight AS weight
FROM lax.high_schools hs
  RIGHT OUTER JOIN lax.hs_ranks hr ON hs.id = hr.hs_id
WHERE 
  hr.gender = 'boy'
  AND hr.year = 2016
  AND hr.rank <= 1500
  AND hs.latitude IS NOT NULL
ORDER BY hr.rank;

-- test creating rank views
SELECT 
  hr.year,
  hr.gender,
  hr.rank,
  hs.raw_name || ', ' || hs.state || ', ' || hs.country,
  hr.zipf_weight,
  hs.latitude,
  hs.longitude
FROM lax.high_schools hs
  INNER JOIN lax.hs_ranks hr ON hs.id = hr.hs_id
WHERE 
  hr.gender = 'boy'
  AND hr.year = 2016
  AND hr.rank <= 1500
  AND hs.geolocated = True
ORDER BY hr.rank;



-- desired rows
SELECT DISTINCT
  raw_hs_name,
  state
FROM lax.hs_ranks
WHERE rank <= 1500
AND state = 'MD';
