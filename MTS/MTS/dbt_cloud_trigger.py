from dagster import job, op, resource
import requests
import os
 
 
@resource()
def dbt_cloud_resource(_):
    def trigger_job():
        headers = {
            "Authorization": f"Bearer {os.getenv('DBT_API_TOKEN')}",  # Using Bearer token
            "Content-Type": "application/json",
        }
 
        # Ensure the correct base URL
 
        url = f"https://lp589.us1.dbt.com/api/v2/accounts/{os.getenv('DBT_ACCOUNT_ID')}/jobs/{os.getenv('DBT_JOB_ID')}/run/"
 
        # Request payload with 'cause' field
 
        data = {"cause": "Triggering job from Dagster"}  # Add a meaningful cause
 
        # Making the POST request with the 'cause' data in the body
 
        response = requests.post(
            url, headers=headers, json=data
        )  # Using 'json' to send the body as JSON
 
        # Handling the response
 
        response.raise_for_status()
        return response.json()
 
    return {"trigger_job": trigger_job}
 
 
@op(required_resource_keys={"dbt_cloud"})
def trigger_dbt_job(context):
    # Trigger the DBT job and log the result
 
    result = context.resources.dbt_cloud["trigger_job"]()
    context.log.info(f"DBT Cloud Job Triggered: {result}")
 
 
@job(resource_defs={"dbt_cloud": dbt_cloud_resource})
def run_dbt_from_dagster():
    trigger_dbt_job()