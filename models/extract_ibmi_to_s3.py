import jaydebeapi
import jpype
import pandas as pd
import boto3
from io import StringIO
import os

def model(dbt, session):
    # Params from environment variables
    jdbc_driver_path = "/dbt/driver/jt400-21.0.3.jar"
    jdbc_url = "jdbc:as400://192.168.1.250"
    user = os.getenv("IBM_I_USER")
    password = os.getenv("IBM_I_PASSWORD")
    driver_class = "com.ibm.as400.access.AS400JDBCDriver"

    if not jpype.isJVMStarted():
        jpype.startJVM(classpath=[jdbc_driver_path])

    conn = jaydebeapi.connect(driver_class, jdbc_url, [user, password], jdbc_driver_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM HALPROD.HALACNL1")
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=columns)

    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)

    s3 = boto3.client('s3')
    s3.put_object(
        Bucket='dynpro-mts',
        Key='HALACNL1.csv',
        Body=csv_buffer.getvalue()
    )

    dbt.log("Uploaded to s3://dynpro-mts/HALACNL1.csv")

    cursor.close()
    conn.close()

    return df.head(5)  # Return small sample to dbt logs
