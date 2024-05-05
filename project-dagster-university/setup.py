from setuptools import find_packages, setup

setup(
    name="dagster_university",
    packages=find_packages(exclude=["dagster_university_tests"]),
    install_requires=[
        "dbt-bigquery==1.7.8",
        "dagster-dbt",
        "dbt-core==1.7.14",
        "dagster-webserver",
        "geopandas",
        "kaleido",
        "pandas[parquet]",
        "plotly",
        "shapely",
        "smart_open[s3]",
        "s3fs",
        "smart_open",
        "boto3",
        "pyarrow",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
