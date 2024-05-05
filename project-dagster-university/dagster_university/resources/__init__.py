from dagster_dbt import DbtCliResource

from ..assets.constants import DBT_DIRECTORY
# the import lines go at the top of the file

# this can be defined anywhere below the imports
dbt_resource = DbtCliResource(
    project_dir=DBT_DIRECTORY,
)
