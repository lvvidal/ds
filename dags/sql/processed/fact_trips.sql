CREATE TABLE IF NOT EXISTS datasprints.fact_trips
WITH (
     format = 'TEXTFILE', 
     field_delimiter = '|',
     external_location = 's3://data-sprints-candidate-luizvidal/data/FACT_TRIPS/',
     partitioned_by = array['dt_obs'])
AS
SELECT vendor_id
	, cast(regexp_replace(substr(pickup_datetime,1,19),'T',' ')  as timestamp) as "pickup_datetime"
	, cast(regexp_replace(substr(dropoff_datetime,1,19),'T',' ')  as timestamp) as "dropoff_datetime"
	, date_diff('minute', cast(regexp_replace(substr(pickup_datetime,1,19),'T',' ')  as timestamp) , cast(regexp_replace(substr(dropoff_datetime,1,19),'T',' ')  as timestamp)) "trip_duration"
	, cast (passenger_count as integer) as "passenger_count"
	, cast(trip_distance as decimal(15,2)) as "trip_distance"
	, pickup_longitude
	, pickup_latitude
	, rate_code
	, store_and_fwd_flag
	, dropoff_longitude
	, dropoff_latitude
	, upper(payment_type) as "payment_type"
	, fare_amount
	, cast(surcharge as decimal(15,2)) as "surcharge"
	, cast(tip_amount as decimal(15,2)) as "tip_amount"
	, cast(tolls_amount as decimal(15,2)) as "tolls_amount"
	, cast(total_amount as decimal(15,2)) as "total_amount"
FROM datasprints.trips;
