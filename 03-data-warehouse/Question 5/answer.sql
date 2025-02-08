CREATE TABLE IF NOT EXISTS `de-zoomcamp-450307.zoomcamp.yellow_tripdata_2024_part_and_clust`
PARTITION BY
  date(tpep_dropoff_datetime) 
CLUSTER BY
  VendorID
AS (
SELECT * 
FROM `de-zoomcamp-450307.zoomcamp.yellow_tripdata_2024_ext`
);


