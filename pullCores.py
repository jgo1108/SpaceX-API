import requests
import pandas as pd

# 1. Fetch data from the API
response = requests.get("https://api.spacexdata.com/v4/cores")
cores = response.json()

# 2. Extract the fields you care about
data = []
for core in cores:
    data.append({
        "Serial": core.get("serial"),
        "Status": core.get("status"),
        "Block": core.get("block"),
        "Reuse_Count": core.get("reuse_count"),  # fixed spelling + case
        "RTLS_Attempts": core.get("rtls_attempts"),
        "RTLS_Landings": core.get("rtls_landings"),
        "ASDS_Attempts": core.get("asds_attempts"),
        "ASDS_Landings": core.get("asds_landings"),
        "Last_Update": core.get("last_update"),
        "ID": core.get("id"),
        "Launches": core.get("launches"),  # this will be a list of IDs
    })

# 3. Convert to a DataFrame and export to Excel
df = pd.DataFrame(data)
df.to_excel("spacex_cores.xlsx", index=False)
print("Done! Saved to spacex_cores.xlsx")