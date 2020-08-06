CREATE TABLE IF NOT EXISTS datasprints.dim_date
WITH (
     format = 'TEXTFILE', 
     field_delimiter = '|',
     external_location = 's3://data-sprints-candidate-luizvidal/data/DIM_DATE/')
AS
SELECT cast(date_format(datas,'%Y%m%d') as bigint) AS "d_key"
       , date_format(datas,'%Y-%m-%d') as "d_data"
       , d.type as "d_feriado"
       , cast(date_format(datas, '%M') as varchar(10)) AS "d_mes"
       , cast(month(datas) as smallint) AS "d_nr_mes"
       , cast(date_format(datas,'%b') as char(3)) AS "d_mes_abrv"
       , concat('Q' , cast(quarter(datas) as varchar(1))) AS "d_trimestre"
       , cast(quarter(datas) as smallint) AS "d_nr_trimestre"
       , year(datas) AS "d_ano"    
       , date_format(datas,'%Y%m') AS "d_ano_mes"   
       , cast(week(datas) as smallint) AS "d_semana"
       , cast(date_format(datas, '%W') as varchar(10)) AS "d_dia"
       , cast(date_format(datas, '%a') as char(3)) AS "d_dia_abrv"
       , cast(dow(datas) as smallint) AS "d_dia_da_semana"
       , cast(day(datas) as smallint) AS "d_dia_do_mes"
       , cast(doy(datas) as smallint) AS "d_dia_do_ano"
       , case 
         when cast(dow(datas) as smallint) in (6,7) then 'false'
         else 'true'
       end AS "d_chk_diadesemana"
       , case 
         when cast(dow(datas) as smallint) in (6,7) then 'true'
         else 'false'
       end AS "d_chk_finaldesemana"
       , case 
         when cast(dow(datas) as smallint) = 1 then 'true'
         else 'false'
       end AS "d_chk_iniciosemana"
       , case
         when cast(dow(datas) as smallint) = 7 then 'true'
         else 'false'
       end AS "d_chk_terminosemana"
       , case 
         when datas = date_trunc('month', datas) then 'true'
         else 'false'
       end AS "d_chk_iniciomes"
       , case 
         when datas = date_trunc('month', datas) + interval '1' month - interval '1' day then 'true'
         else 'false'
       end AS "d_chk_fimmes"
       , case 
         when datas = date_trunc('quarter', datas) then 'true'
         else 'false'
       end AS "d_chk_iniciotrimestre"
       , case 
         when datas = date_trunc('quarter', datas) + interval '3' month - interval '1' day then 'true'
         else 'false'
       end AS "d_chk_fimtrimestre" 
       , case
         when (year(datas) % 4 = 0 AND year(datas) % 100 <> 0) OR year(datas) % 400 = 0 then 'true'
         else 'false'
       end AS "d_chk_anobissexto"
       , case
         when (d.type is null) then 'false'
         else 'true'
       end AS "d_chk_feriado"
FROM(
SELECT datas ,h.type
	FROM UNNEST(SEQUENCE(
        DATE('2009-01-01'), 
        DATE_TRUNC('day', DATE('2012-12-31')), 
        INTERVAL '1' DAY)) as d("datas")
LEFT JOIN ( SELECT 
				x.n['type'] as "type",
				x.n['day'] as "day"
		    FROM UNNEST (
				CAST(JSON_EXTRACT('{"payload":[{"day":"0101","type":"Ano Novo"},{"day":"0421","type":"Tiradentes"},
                        {"day":"0501","type":" Dia do Trabalho"},{"day":"0907","type":"Dia da Independência"},
                        {"day":"1012","type":"Nossa Senhora Aparecida"},{"day":"1102","type":"Dia de Finados"},
                        {"day":"1115","type":"Proclamação da República"},{"day":"1225","type":"Natal"}]}',
                        '$.payload') 
					 AS ARRAY<MAP<VARCHAR, VARCHAR>>
					)
				) 
			AS x(n)
		) AS h ON (date_format(datas,'%m%d') = h.day)
) as d 
ORDER BY 1 ASC;