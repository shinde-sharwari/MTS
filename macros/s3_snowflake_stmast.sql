-- macros/mts_bronze_stmast_data.sql
{% macro mts_bronze_stmast_data() %}
    {% do run_query(
        "COPY INTO BOOTCAMP.MTS_BRONZE.T_BRZ_STORE_MASTER_STMAST
            FROM @MTS_RAW.STG_MTS_IBMI_S3_RAW_EXT/in
            FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY='\"' SKIP_HEADER=1)"
    ) %}
{% endmacro %}
