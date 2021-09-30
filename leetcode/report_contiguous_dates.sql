--LC 1225: Report Contiguous Data

with
    raw_periods as (
        select
            'succeeded' as period_state,
            success_date as period_date,
            row_number() over (order by success_date asc) as rownum
        from succeeded
        where success_date between str_to_date('2019-01-01', '%Y-%m-%d') and str_to_date('2019-12-31', '%Y-%m-%d')
        union
        select
            'failed' as period_state,
            fail_date as period_date,
            row_number() over (order by fail_date asc) as rownum
        from failed
        where fail_date between str_to_date('2019-01-01', '%Y-%m-%d') and str_to_date('2019-12-31', '%Y-%m-%d')
    ),
    grouping_dates as (
        select
            period_state,
            period_date,
            date_add(period_date, interval -rownum day) as grouping_date,
        from raw_periods
    ),
    start_dates as(
        select
            period_state,
            min(period_date) as start_date,
            count(*)
        from grouping_dates
        group by grouping_date, period_state
    )
select
    period_state,
    start_date,
    date_add(start_date, interval period_count-1 day) as end_date
from start_dates
order by start_date asc