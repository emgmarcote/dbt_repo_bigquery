from dagster import Definitions, load_assets_from_modules

from .assets import dbt # Import the dbt assets
from .resources import dbt_resource # import the dbt resource
# ...other existing imports

# ... existing calls to load_assets_from_modules
dbt_analytics_assets = load_assets_from_modules(modules=[dbt]) # Load the assets from the file

# ... other declarations

defs = Definitions(
    assets=[*dbt_analytics_assets], # Add the dbt assets to your code location
    resources={
        "dbt": dbt_resource # register your dbt resource with the code location
    },
  # .. other definitions
)
