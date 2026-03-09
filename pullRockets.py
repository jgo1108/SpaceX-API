import requests
import pandas as pd

# 1. Fetch rockets data
response = requests.get("https://api.spacexdata.com/v4/rockets")
rockets = response.json()

# 2. Extract fields (including nested ones)
data = []
for rocket in rockets:
    data.append({
        "Name": rocket.get("name"),
        "Type": rocket.get("type"),
        "Active": rocket.get("active"),
        "Stages": rocket.get("stages"),
        "Boosters": rocket.get("boosters"),
        "Cost_Per_Launch": rocket.get("cost_per_launch"),
        "Success_Rate_Pct": rocket.get("success_rate_pct"),
        "First_Flight": rocket.get("first_flight"),
        "Country": rocket.get("country"),
        # Nested fields - need to go one level deeper
        "Height_Meters": rocket.get("height", {}).get("meters"),
        "Diameter_Meters": rocket.get("diameter", {}).get("meters"),
        "Mass_KG": rocket.get("mass", {}).get("kg"),
        "Engine_Type": rocket.get("engines", {}).get("type"),
        "Engine_Count": rocket.get("engines", {}).get("number"),
        "Propellant_1": rocket.get("engines", {}).get("propellant_1"),
        "Propellant_2": rocket.get("engines", {}).get("propellant_2"),
        "First_Stage_Reusable": rocket.get("first_stage", {}).get("reusable"),
        "First_Stage_Engines": rocket.get("first_stage", {}).get("engines"),
        "Description": rocket.get("description"),
        "ID": rocket.get("id"),
    })

# 3. Export to Excel
df = pd.DataFrame(data)
df.to_excel("spacex_rockets.xlsx", index=False)
print("Done! Saved to spacex_rockets.xlsx")