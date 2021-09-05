with a as (
	select salesperson_id, max(amount) as max_amount
	from orders
	group by salesperson_id
)
select b.salesperson_id, b.order_date, b.customer_id, b.number
from orders b
join a
on b.salesperson_id = a.salesperson_id and b.amount = a.amount