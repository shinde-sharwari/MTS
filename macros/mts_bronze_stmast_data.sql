{% macro mts_bronze_stmast_data() %}
    {% set sql %}
        COPY INTO BOOTCAMP.MTS_BRONZE.T_BRZ_STORE_MASTER_STMAST FROM(
            SELECT
    $1  AS A4STORE,
    $2  AS A4PSTN,
    $3  AS A4NAME,
    $4  AS A4ADR1,
    $5  AS A4ADR2,
    $6  AS A4ADR3,
    $7  AS A4CITY,
    $8  AS A4STAT,
    $9  AS A4ZIP,
    $10 AS A4FDID,
    $11 AS A4STID,
    $12 AS A4WIPX,
    $13 AS A4LO,
    $14 AS A4CO,
    $15 AS A4MSWX,
    $16 AS A4MWST,
    $17 AS A4TERR,
    $18 AS A4USER,
    $19 AS A4CYMD,
    $20 AS A4HMS,
    $21 AS A4WKSN,
    $22 AS A4PHN1,
    $23 AS A4PEX1,
    $24 AS A4PHN2,
    $25 AS A4PEX2,
    $26 AS A4PHN3,
    $27 AS A4PEX3,
    $28 AS A4FAX,
    $29 AS A4PRT,
    $30 AS A4TDCD,
    null as PROD_DT,
    CURRENT_TIMESTAMP as LOAD_DTTM
FROM @MTS_RAW.STG_MTS_IBMI_S3_RAW_EXT/in/
        )
 FILE_FORMAT = MTS_BRONZE.MY_CSV_FORMAT;
    {% endset %}
 
    {{ run_query(sql) }}
{% endmacro %}