


{{ config(materialized='table') }}  
 
WITH debug_data AS (
    {{ externalstagetosnf() }}  
)
 
SELECT * FROM debug_data