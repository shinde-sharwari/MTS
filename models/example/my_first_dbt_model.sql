
{{ config(materialized='table') }}

with source_data as (

    select * from BOOTCAMP.MTS_RAW.MY_FIRST_DBT_MODEL

)

select *
from source_data
