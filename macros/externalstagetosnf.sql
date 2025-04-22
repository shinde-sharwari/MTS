-- macros/externalstagetosnf.sql

{% macro externalstagetosnf() %}

{% set mappings = [
    {'file_pattern': '.*sales_data.*\\.csv', 'target_table': 'MTS_SALES_DATA'}
] %}

{% for mapping in mappings %}
    {% set sql %}
        COPY INTO BOOTCAMP.MTS_RAW.{{ mapping.target_table }}
        FROM @MTS_RAW.MTS_RAW_STAGE
        FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY='"' SKIP_HEADER=1)
        PATTERN = '{{ mapping.file_pattern }}';
    {% endset %}

    {{ log("Running copy for: " ~ mapping.target_table, info=True) }}
    {{ run_query(sql) }}

{% endfor %}

{% endmacro %}