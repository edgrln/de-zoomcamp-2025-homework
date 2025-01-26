


SELECT 
CONCAT(zpu."Borough", ' / ', zpu."Zone") as "pickup_loc" 

,sum(total_amount) as total_amount
--CONCAT(zdo."Borough", ' / ', zdo."Zone") as "dropoff_loc" 
FROM public.yellow_taxi_trips t 
JOIN zones zpu ON t."PULocationID"  = zpu."LocationID"
--JOIN zones zdo ON t."DOLocationID"  = zdo."LocationID"
where cast(lpep_pickup_datetime as Date) = '2019-10-18' 
group by 1
having(sum(total_amount) > 13000)
order by total_amount desc
limit 100;