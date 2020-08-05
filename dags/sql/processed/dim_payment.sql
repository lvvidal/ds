CREATE TABLE IF NOT EXISTS datasprints.dim_payment
WITH (
     format = 'TEXTFILE', 
     field_delimiter = '|',
     external_location = 's3://data-sprints-candidate-luizvidal/data/DIM_PAYMENT/')
AS
SELECT row_number() over (partition by payment_lookup ) as "payment_seq", *
FROM
	(	
	SELECT  distinct(upper(payment_type)) as "payment_type", payment_lookup
	FROM datasprints.payment
	WHERE upper(payment_lookup) <> 'FOO'
	)
order by 3,1;