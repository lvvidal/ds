CREATE EXTERNAL TABLE `datasprints.trips_streaming`(
  `vendor_id` string COMMENT 'vendor_id', 
  `pickup_datetime` string COMMENT 'pickup_datetime', 
  `dropoff_datetime` string COMMENT 'dropoff_datetime', 
  `passenger_count` string COMMENT 'passenger_count', 
  `trip_distance` string COMMENT 'trip_distance', 
  `pickup_longitude` string COMMENT 'pickup_longitude', 
  `pickup_latitude` string COMMENT 'pickup_latitude', 
  `rate_code` string COMMENT 'rate_code', 
  `store_and_fwd_flag` string COMMENT 'store_and_fwd_flag', 
  `dropoff_longitude` string COMMENT 'dropoff_longitude', 
  `dropoff_latitude` string COMMENT 'dropoff_latitude', 
  `payment_type` string COMMENT 'payment_type', 
  `fare_amount` string COMMENT 'fare_amount', 
  `surcharge` string COMMENT 'surcharge', 
  `tip_amount` string COMMENT 'tip_amount', 
  `tolls_amount` string COMMENT 'tolls_amount', 
  `total_amount` string COMMENT 'total_amount')
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.serde2.OpenCSVSerde' 
WITH SERDEPROPERTIES ( 
  'escapeChar'='\\', 
  'quoteChar'='\"', 
  'separatorChar'=',') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://data-sprints-candidate-luizvidal/streaming/trips'
TBLPROPERTIES (
  'areColumnsQuoted'='false', 
  'classification'='csv', 
  'columnsOrdered'='true', 
  'delimiter'=',', 
  'typeOfData'='file')