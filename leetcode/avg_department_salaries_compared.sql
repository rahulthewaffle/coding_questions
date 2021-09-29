-- LC # 615


with pay_averages as (
	select 
		date_format(s.pay_date, '%Y-%m') as pay_month,
		e.department_id,
		avg(s.amount) over (partition by date_format(s.pay_date, '%Y-%m'), e.department_id) as dept_average,
		avg(s.amount) over (partition by date_format(s.pay_date, '%Y-%m')) as company_average
	from employee as e
	inner join salary as s
	on e.employee_id = s.employee_id
)
select
	pay_month,
	department_id,
	case 
		when dept_average < company_average then 'lower'
		when dept_average = company_average then 'same'
		when dept_average > company_average then 'higher'
	end as comparison
from pay_averages
group by pay_month, department_id, comparison
order by pay_month desc, department_id asc