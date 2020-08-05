-- Qual a distância média percorrida por viagens com no máximo 2 passageiros;
select avg(trip_distance)
from datasprints.fact_trips 
where passenger_count = 2;

-- Quais os 3 maiores vendors em quantidade total de dinheiro arrecadado;

select sum(ft.total_amount) as "total", dv.vendor_id || ' - ' || dv.name as "vendor"
from datasprints.fact_trips ft
inner join datasprints.dim_vendor dv
	on (dv.vendor_id = ft.vendor_id)
group by 2
order by 1 desc;

--Faça um histograma da distribuição mensal, nos 4 anos, de corridas pagas em dinheiro;
select count(*) as "total", date_format(cast(ft.pickup_datetime as date),'%Y-%m') as  "anomes"
from datasprints.fact_trips ft
where ft.payment_type = 'CASH'
group by 2
order by 2 desc;

--Faça um gráfico de série temporal contando a quantidade de gorjetas de cada dia, nos últimos 3 meses de 2012.
select sum(t1.total) , t1.tip_date
from (
	select ft.tip_amount as "total"
			, dense_rank() over (order by date_format(cast(ft.pickup_datetime as date),'%Y-%m') desc) as "last3"
			, date_format(cast(ft.pickup_datetime as date),'%Y-%m-%d') as "tip_date"
	from datasprints.fact_trips ft
	where ft.year = 2012 
	) as t1 
where t1.last3 <= 3
group by 2
order by 2 desc;

-- Qual o tempo médio das corridas nos dias de sábado e domingo;
select avg(trip_duration) "tempo_medio", d.d_dia 
from datasprints.fact_trips ft
inner join datasprints.dim_date d
	on (date_format(cast(ft.pickup_datetime as date),'%Y-%m-%d') = d.d_data)
where d.d_dia in ('Saturday', 'Sunday')
group by 2;
