-- macros/load_mts_sales_data.sql
{% macro load_mts_sales_data() %}
    COPY INTO BOOTCAMP.MTS_RAW.MTS_SALES_DATA
    FROM @MTS_RAW.MTS_RAW_STAGE
    FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY='"' SKIP_HEADER=1)
{% endmacro %}
