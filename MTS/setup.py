from setuptools import find_packages, setup

setup(
    name="MTS",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        "MTS": [
            "dbt-project/**/*",
        ],
    },
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-snowflake<1.10",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)

