import requests
import os
from dagster import op

@op
def trigger_dbt_cloud_job():
    job_id = "YOUR_DBT_JOB_ID"
    account_id = "YOUR_ACCOUNT_ID"
    dbt_token = os.getenv("DBT_CLOUD_API_TOKEN")

    headers = {"Authorization": f"Token {dbt_token}"}
    url = f"https://cloud.getdbt.com/api/v2/accounts/{account_id}/jobs/{job_id}/run/"
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        print("✅ Triggered dbt Cloud job successfully")
    else:
        raise Exception(f"❌ Failed to trigger dbt job: {response.text}")
