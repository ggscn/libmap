WITH
  book_locations AS (
  SELECT
    BookMeta_Title,
    BookMeta_Author,
    SPLIT(V2Locations,';') AS locations
  FROM
    gdelt-bq.hathitrustbooks.1800)
SELECT
  BookMeta_Title,
  BookMeta_Author,
  locations,
  ROUND(CAST(REGEXP_EXTRACT(locations,r'^[2-5]#.*?#.*?#.*?#.*?#(.*?)#.*?#') as FLOAT64),3) AS lat,
  ROUND(CAST(REGEXP_EXTRACT(locations,r'^[2-5]#.*?#.*?#.*?#.*?#.*?#(.*?)#') as FLOAT64),3) AS long,
  REGEXP_EXTRACT(locations,r'^[2-5]#(.*?)#.*?#.*?#.*?#.*?#.*?#') as name
FROM
  book_locations,
  UNNEST(locations) AS locations
WHERE BookMeta_Title like '%{}%' or BookMeta_Author like '%{}%'