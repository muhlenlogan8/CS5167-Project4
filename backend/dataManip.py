import pandas as pd
import json
import math

file = "data.csv"
output = "scatter_data.json"
sheet = 0

df = pd.read_csv(file, comment="#", skip_blank_lines=True, on_bad_lines="skip")

def toNumber(x):
    if pd.isna(x):
        return None
    try:
        return float(str(x).replace(",", "").strip())
    except ValueError:
        return None

def clean(x):
    if x is None or pd.isna(x) or (isinstance(x, float) and math.isnan(x)):
        return None
    return x

df["energy_gj"] = df["Energy use per capita (GJ)"].apply(toNumber)
df["life_expectancy"] = df["Life expectancy"].apply(toNumber)
df["population"] = df["Population"].apply(toNumber)

data = []

for _, row in df.iterrows():
    entry = {
        "country": row["Country"],
        "code": row["Code"],
        "year": int(row["Year"]),
        "energy_gj": clean(row["energy_gj"]),
        "life_expectancy": clean(row["life_expectancy"]),
        "population": int(clean(row["population"])) if clean(row["population"]) else None,
        "continent": row["Continent"],
    }

    data.append(entry)

with open(output, "w") as f:
    json.dump(data, f, indent=4)

print("Done")