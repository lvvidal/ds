CREATE TABLE IF NOT EXISTS datasprints.dim_vendor
WITH (
     format = 'TEXTFILE', 
     field_delimiter = '|',
     external_location = 's3://data-sprints-candidate-luizvidal/data/DIM_VENDOR/')
AS
SELECT upper(vendor_id) as "vendor_id"
		, name
		, address
		, city
		, cast(state as char(2)) as "state"
		, cast(zip as integer) as "zip"
		, cast(country as char(3)) as "country"
		, contact
		, case 
			when "current" = 'Yes' then true
			else false
		end as "current"
FROM datasprints.vendor;