--LC 1225: Report Contiguous Data

with
    raw_periods as (
        select
            'succeeded' as period_state,
            success_date as period_date,
            row_number() over (partition by success_date order by success_date desc) as rownum
        from succeeded
        where success_date between date('2019-01-01', '%Y-%m-%d') and date('2019-12-31', '%Y-%m-%d')
        union
        select
            'failed' as period_state,
            fail_date as period_date,
            row_number() over (partition by success_date order by success_date desc) as rownum
        from failed
        where fail_date between date('2019-01-01', '%Y-%m-%d') and date('2019-12-31', '%Y-%m-%d')
    ),
    start_dates as (
        select
            period_state,
            dateadd('day', rownum, period_date) as start_date,
            count(*) as period_count
        from raw_periods
        group by period_state, dateadd('day', rownum, period_date)
    )
select
    period_state,
    start_date,
    dateadd('day', period_count, start_date) as end_date
from start_dates
order by start_date asc