-- macros/mts_bronze_stmast_data.sql
{% macro mts_bronze_stmast_data() %}
    {% set sql %}
        COPY INTO BOOTCAMP.MTS_RAW.T_BRZ_WORK_ORDER_HEADER_WOMSTH
        FROM @MTS_RAW.STG_MTS_IBMI_S3_RAW_EXT/in
        FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY='"' SKIP_HEADER=1)';
    {% endset %}
 
    {{ run_query(sql) }}
 
{% endmacro %}
