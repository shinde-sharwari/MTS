from dagster import asset
import jaydebeapi
import jpype
import pandas as pd
import boto3
from io import StringIO

@asset
def fetch_as400_to_s3():
    jdbc_driver_path = "C:/Users/Sharwari Shinde/Downloads/jt400-21.0.3.jar"
    jdbc_url = "jdbc:as400://192.168.1.250"
    user = "SHARWARIS"
    password = "DYN007"
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
    bucket_name = 'dynpro-mts'
    s3.put_object(Bucket=bucket_name, Key='HALACNL1.csv', Body=csv_buffer.getvalue())

    print("Uploaded to s3://dynpro-mts")

    cursor.close()
    conn.close()