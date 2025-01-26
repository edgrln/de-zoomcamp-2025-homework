select trip_distance_type, count(1)
from
(
SELECT 
CASE 
when trip_distance <= 1 then 1 --'up_to_1_mile'
when trip_distance > 1 and trip_distance <= 3 then 2 --'in_between_1_exclusive_and_3_miles_inclusive'
when trip_distance > 3 and trip_distance <= 7 then 3 --'in_between_3_exclusive_and_7_miles_inclusive'
when trip_distance > 7  and trip_distance <= 10 then 4 --'in_between_7_exclusive_and_10_miles_inclusive'
when trip_distance  > 10 then 5 --'over_10_miles'
End as trip_distance_type
FROM public.yellow_taxi_trips
where cast(lpep_pickup_datetime as Date) >= '2019-10-01' and  cast(lpep_dropoff_datetime as Date) < '2019-11-01'
) tmp
group by 1
