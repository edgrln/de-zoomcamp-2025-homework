SELECT 

zdo."Zone"  
, max(tip_amount)

FROM public.yellow_taxi_trips t 
JOIN zones zpu ON t."PULocationID"  = zpu."LocationID"
JOIN zones zdo ON t."DOLocationID"  = zdo."LocationID"
where cast(lpep_pickup_datetime as date) >= '2019-10-01' and cast(lpep_pickup_datetime as date) < '2019-11-30' and zpu."Zone" ='East Harlem North'
group by 1
order by max(tip_amount) desc
limit 1

