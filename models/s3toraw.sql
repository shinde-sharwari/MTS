{{ config(materialized='table') }}  
 
WITH debug_data AS (
    {{ load_mts_sales_data() }}  
)
 
SELECT * FROM debug_data