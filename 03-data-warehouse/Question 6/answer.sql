SELECT count(distinct VendorID)
FROM `de-zoomcamp-450307.zoomcamp.yellow_tripdata_2024` 
where tpep_dropoff_datetime between '2024-03-01' and '2024-03-15';



SELECT count(distinct VendorID)
FROM `de-zoomcamp-450307.zoomcamp.yellow_tripdata_2024_part_and_clust` 
where tpep_dropoff_datetime between '2024-03-01' and '2024-03-15';