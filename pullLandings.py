import requests
import pandas as pd

# 1. Fetch data from the API
response = requests.get("https://api.spacexdata.com/v5/launches")
launches = response.json()

# 2. Extract the fields you care about
data = []
for launch in launches:
    data.append({
        "Name": launch.get("name"),
        "Date": launch.get("date_utc"),
        "Success": launch.get("success"),
        "Rocket": launch.get("rocket"),
        "Flight Number": launch.get("flight_number"),
        "Details": launch.get("details"),
        "Launchpad": launch.get("launchpad"),
    })

# 3. Convert to a DataFrame and export to Excel
df = pd.DataFrame(data)
df.to_excel("spacex_launches.xlsx", index=False)
print("Done! Saved to spacex_launches.xlsx")