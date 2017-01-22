-- Find top-20 high schools that have not been geolocated
-- 22 schools in the top 25 that were not automatically geocoded
SELECT id, raw_name || ', ' || state || ' ' || country
FROM lax.high_schools
WHERE geolocated = False 
AND id IN (
    SELECT DISTINCT hs_id
    FROM lax.hs_ranks
    WHERE rank <= 100)
 ORDER BY id;

-- Manually geocode themUPDATE lax.high_schoolsUPDATE lax.high_schools
UPDATE lax.high_schools
SET searched_name = '2804 Holicong Rd, Doylestown',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 4861;

UPDATE lax.high_schools
SET searched_name = '6575 N Kendall Dr, Pinecrest',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 4644;

UPDATE lax.high_schools
SET searched_name = '2132 Ivy Rd, Charlottesville',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 4402;

UPDATE lax.high_schools
SET searched_name = '888 Brett Ln, Saltsburg',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 4279;

UPDATE lax.high_schools
SET searched_name = '378 Main St, Shrewsbury',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 4267;

UPDATE lax.high_schools
SET searched_name = '1733 W Girard Ave, Philadelphia',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 4210;

UPDATE lax.high_schools
SET searched_name = '101 N Warson Rd, St. Louis',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 4005;

UPDATE lax.high_schools
SET searched_name = '3001 Wisconsin Ave NW, Washington',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 3873;

UPDATE lax.high_schools
SET searched_name = '2815 Benade Cir, Bryn Athyn',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 3774;

UPDATE lax.high_schools
SET searched_name = '9101 Rockville Pike Bethesda',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 3660;

UPDATE lax.high_schools
SET searched_name = '6269 El Fuerte St, Carlsbad',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 3630;

UPDATE lax.high_schools
SET searched_name = '601 McKinley Pkwy, Buffalo',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 3573;

UPDATE lax.high_schools
SET searched_name = '2001 37th Ave, San Francisco',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 3509;

UPDATE lax.high_schools
SET searched_name = '101 N Warson Rd, St. Louis',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 3423;

UPDATE lax.high_schools
SET searched_name = '700 Academy Rd, Catonsville',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 3349;


UPDATE lax.high_schools
SET searched_name = '3400 Lambkin Way Fort Collins',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 3203;

UPDATE lax.high_schools
SET searched_name = '800 Clapboardtree St, Westwood',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 3082;

UPDATE lax.high_schools
SET searched_name = '90 Grovers Mill Road Plainsboro Township',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 3064;

UPDATE lax.high_schools
SET searched_name = '1340 S Valley Forge Rd, Lansdale',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 2625;

UPDATE lax.high_schools
SET searched_name = '120 Northfield Ave, West Orange',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 2611;

UPDATE lax.high_schools
SET searched_name = '2132 Ivy Rd, Charlottesville',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 2602;

UPDATE lax.high_schools
SET searched_name = '145 Plainfield Ave, Metuchen',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 2590;

UPDATE lax.high_schools
SET searched_name = '901 Highland Ave, Orlando',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 2489;

UPDATE lax.high_schools
SET searched_name = '72 Spring St, Danvers',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 2479;

UPDATE lax.high_schools
SET searched_name = '90 Grovers Mill Road, Plainsboro',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 2477;

UPDATE lax.high_schools
SET searched_name = 'Greenlawn',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 2416;

UPDATE lax.high_schools
SET searched_name = '220 Woodbine Rd, Downingtown',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 2411;

UPDATE lax.high_schools
SET searched_name = '700 Academy Rd, Catonsville',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 2390;

UPDATE lax.high_schools
SET searched_name = '9301 State Line Rd, Kansas City',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 2325;

UPDATE lax.high_schools
SET searched_name = '1850 De La Salle Dr, St. Louis',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 2269;

UPDATE lax.high_schools
SET searched_name = '3101 Wisconsin Ave, Washington',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 2255;

UPDATE lax.high_schools
SET searched_name = '4653 Clairton Blvd, Pittsburgh',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 2182;

UPDATE lax.high_schools
SET searched_name = '2600 Rutherford Rd, Concord',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 2083;

UPDATE lax.high_schools
SET searched_name = '1130 Winton Dr, Concord',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 1908;

UPDATE lax.high_schools
SET searched_name = '22600 Camp Calvert Rd, Leonardtown',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 1842;

UPDATE lax.high_schools
SET searched_name = '6245 Randall Rd, Syracuse',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 1802;

UPDATE lax.high_schools
SET searched_name = '6245 Randall Rd, Syracuse',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 1683;

UPDATE lax.high_schools
SET searched_name = '612 Academy Ave, Providence',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 1656;

UPDATE lax.high_schools
SET searched_name = '441 E Fordham Rd, Bronx',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 1648;

UPDATE lax.high_schools
SET searched_name = '2320 Huntington Turnpike, Trumbull',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 1444;

UPDATE lax.high_schools
SET searched_name = '2320 Huntington Turnpike, Trumbull',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 1444;

UPDATE lax.high_schools
SET searched_name = '91 Haddington St, Caledonia',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 1419;

UPDATE lax.high_schools
SET searched_name = '1191 Greendale Ave, Needham',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 1401;

UPDATE lax.high_schools
SET searched_name = '6245 Randall Rd, Syracuse',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 172;

UPDATE lax.high_schools
SET searched_name = '850 Newman Springs Rd, Lincroft',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 1365;

UPDATE lax.high_schools
SET searched_name = '1345 Easton Ave, Somerset',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 1159;

UPDATE lax.high_schools
SET searched_name = '4100 Baldwin Rd, Rushville',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 1109;

UPDATE lax.high_schools
SET searched_name = '700 Stevenson Rd N, Oshawa',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 1043;

UPDATE lax.high_schools
SET searched_name = '1 Maverick Way, Carlsbad',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 965;

UPDATE lax.high_schools
SET searched_name = '560 Sproul Rd, Villanova',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 823;

UPDATE lax.high_schools
SET searched_name = '1401 Edwards Mill Rd, Raleigh',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 798;

UPDATE lax.high_schools
SET searched_name = '900 High St, Easton',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 561;

UPDATE lax.high_schools
SET searched_name = '2132 Ivy Rd, Charlottesville',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 444;

UPDATE lax.high_schools
SET searched_name = '25 Marlboro Rd, Southborough',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 423;

UPDATE lax.high_schools
SET searched_name = '600 W North Bend Rd, Cincinnati',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 386;

UPDATE lax.high_schools
SET searched_name = '5035 Sideburn Rd, Fairfax',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 248;


UPDATE lax.high_schools
SET searched_name = '508 S Main St, Berlin',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 192;

UPDATE lax.high_schools
SET searched_name = 'Dallas Jesuit, TX United States of America',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 115;

UPDATE lax.high_schools
SET searched_name = '611 Cedar Ave, Richland',
geotried_googlev3 = False,
geotried_nominatim = False
WHERE id = 14;

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
