with source as (
      select * from {{ source('DBT', 'src_chicago_crimenes') }}
),
renamed as (
    select *
    from source
)
select * from renamed
  