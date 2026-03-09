import requests
import pandas as pd

# 1. Fetch dragons data
response = requests.get("https://api.spacexdata.com/v4/dragons")
dragons = response.json()

# 2. Extract fields
data = []
for dragon in dragons:
    data.append({
        "Name": dragon.get("name"),
        "Type": dragon.get("type"),
        "Active": dragon.get("active"),
        "Crew_Capacity": dragon.get("crew_capacity"),
        "First_Flight": dragon.get("first_flight"),
        "Orbit_Duration_Yr": dragon.get("orbit_duration_yr"),
        "Dry_Mass_KG": dragon.get("dry_mass_kg"),
        # 2 levels deep
        "Height_w_Trunk_Meters": dragon.get("height_w_trunk", {}).get("meters"),
        "Diameter_Meters": dragon.get("diameter", {}).get("meters"),
        "Launch_Payload_Mass_KG": dragon.get("launch_payload_mass", {}).get("kg"),
        "Return_Payload_Mass_KG": dragon.get("return_payload_mass", {}).get("kg"),
        "Launch_Payload_Vol_M3": dragon.get("launch_payload_vol", {}).get("cubic_meters"),
        "Return_Payload_Vol_M3": dragon.get("return_payload_vol", {}).get("cubic_meters"),
        "Heat_Shield_Material": dragon.get("heat_shield", {}).get("material"),
        "Heat_Shield_Temp": dragon.get("heat_shield", {}).get("temp_degrees"),
        # 3 levels deep
        "Trunk_Vol_M3": dragon.get("trunk", {}).get("trunk_volume", {}).get("cubic_meters"),
        "Solar_Array": dragon.get("trunk", {}).get("cargo", {}).get("solar_array"),
        "Pressurized_Vol_M3": dragon.get("pressurized_capsule", {}).get("payload_volume", {}).get("cubic_meters"),
        "Description": dragon.get("description"),
        "ID": dragon.get("id"),
    })

# 3. Export to Excel
df = pd.DataFrame(data)
df.to_excel("spacex_dragons.xlsx", index=False)
print("Done! Saved to spacex_dragons.xlsx")