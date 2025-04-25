{% macro run_ibmi_script() %}
    {% do run_query('!python3 MTS/MTS/as400_to_s3.py') %}MTS/MTS/as400_to_s3.py
{% endmacro %}
