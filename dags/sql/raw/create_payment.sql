CREATE EXTERNAL TABLE `datasprints.payment`(
  `payment_type` string COMMENT 'payment_type', 
  `payment_lookup` string COMMENT 'payment_lookup')
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
  's3://data-sprints-candidate-luizvidal/batch/payment'
TBLPROPERTIES (
  'areColumnsQuoted'='false', 
  'skip.header.line.count' = '1',
  'classification'='csv', 
  'columnsOrdered'='true', 
  'delimiter'=',', 
  'typeOfData'='file')