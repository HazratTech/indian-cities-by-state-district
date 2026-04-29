from fastapi import FastAPI, HTTPException
import json

app = FastAPI(
    title="Indian Location API",
    description="API for Indian States, Districts, and Cities from combined_data.json",
    version="1.0.0"
)

with open("combined_data.json", "r", encoding="utf-8") as file:
    combined_data = json.load(file)


def normalize_name(name:str):
    return name.strip().lower()

@app.get("/", tags=["Root"])
def root():
    return {"message": "Welcome to the Indian Location API!"}

@app.get("/all", tags=["ALL"])
def get_all():
    return combined_data

@app.get("/states", tags=["States"])
def all_states():
    return list(combined_data.keys())

@app.get("/states/{state_name}", tags=["States"])
def get_state(state_name: str):
    normalize_state = normalize_name(state_name)
    for key in combined_data:
        if normalize_name(key) == normalize_state:
            return {key : combined_data[key]}
    raise HTTPException(status_code=404, detail="State not found")



@app.get("/districts", tags=["Districts"])
def get_all_districts():
    districts = set()
    for state in combined_data.values():
        districts.update(state.keys())
    return sorted(list(districts))

@app.get("/districts/{state}", tags=["Districts"])
def get_districts_by_state(state: str):
    normalized_state = normalize_name(state)
    for key in combined_data:
        if normalize_name(key) == normalized_state:
            return sorted(combined_data[key].keys())
    raise HTTPException(status_code=404, detail="State not found")



@app.get("/cities", tags=["Cities"])
def get_all_cities():
    cities = []

    for state in combined_data.values():
        for city_list in state.values():
            cities.extend(city_list)
    return sorted(cities)

@app.get("/cities/{district_name}", tags=["Cities"])
def get_cities_by_district(district_name: str):
    normalized_district = normalize_name(district_name)
    for state_data in combined_data.values():
        for district, city_list in state_data.items():
            if normalize_name(district) == normalized_district:
                return sorted(city_list)
    raise HTTPException(status_code=404, detail="District not found")