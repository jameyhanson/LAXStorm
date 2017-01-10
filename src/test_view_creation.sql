CREATE TABLE lax.high_schools_bak_20170109 AS
SELECT * FROM lax.high_schools;

-- test creating rank views
SELECT 
  hr.year,
  hr.gender,
  hr.rank,
  hr.raw_hs_name,
  hr.state,
  hs.raw_name,
  hs.state,
  hs.latitude,
  hs.longitude
FROM lax.high_schools hs
  RIGHT OUTER JOIN lax.hs_ranks hr ON hs.id = hr.hs_id
WHERE 
  hr.gender = 'boy'
  AND hr.year = 2003
  AND hr.rank <= 1500
ORDER BY hr.rank;

-- desired rows
SELECT DISTINCT
  raw_hs_name,
  state
FROM lax.hs_ranks
WHERE rank <= 1500
AND state = 'MD';
