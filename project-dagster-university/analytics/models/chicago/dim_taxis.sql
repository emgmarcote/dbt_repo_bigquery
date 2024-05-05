{{
  config(
    materialized = 'table',
    )
}}

select 
distinct
taxi_id,
'No Documentado' as taxi_desc
 from {{ ref('stg_taxi_trips') }}