{{ config(materialized='table') }}

with source_data as (

    COPY INTO BOOTCAMP.MTS_RAW.MTS_SALES_DATA
        FROM @MTS_RAW.MTS_RAW_STAGE
        FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY='"' SKIP_HEADER=1)
)

select *
from source_data