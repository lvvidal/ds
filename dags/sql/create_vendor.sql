CREATE EXTERNAL TABLE `datasprints.vendor`(
  `vendor_id` string COMMENT 'vendor_id', 
  `name` string COMMENT 'name', 
  `address` string COMMENT 'address', 
  `city` string COMMENT 'city', 
  `state` string COMMENT 'state', 
  `zip` string COMMENT 'zip', 
  `country` string COMMENT 'country', 
  `contact` string COMMENT 'contact', 
  `current` string COMMENT 'current')
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
  's3://data-sprints-candidate-luizvidal/batch/vendor'
TBLPROPERTIES (
  'areColumnsQuoted'='false', 
  'skip.header.line.count' = '1',
  'classification'='csv', 
  'columnsOrdered'='true', 
  'delimiter'=',', 
  'typeOfData'='file')