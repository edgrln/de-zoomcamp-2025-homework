
SELECT 
cast(lpep_pickup_datetime as Date) as lpep_pickup_date , 
max(trip_distance) 
FROM public.yellow_taxi_trips
group by 1
order by max(trip_distance) desc
limit 1