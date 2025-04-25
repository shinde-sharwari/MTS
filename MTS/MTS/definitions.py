from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets import my_dbt_project_dbt_assets
from .project import my_dbt_project_project
from .schedules import schedules
from .dbt_cloud_trigger import run_dbt_from_dagster
from jobs.as400_job import fetch_as400_to_s3

defs = Definitions(
    assets=[my_dbt_project_dbt_assets],
    schedules=schedules,
    jobs=[run_dbt_from_dagster,fetch_as400_to_s3],
    resources={
        "dbt": DbtCliResource(project_dir=my_dbt_project_project),
    },
)

