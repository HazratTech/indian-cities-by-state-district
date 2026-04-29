import json

with open('D:\\Coding\\Python\\api\\addrees\\combined_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

cleaned_data = {}
for state, districts in data.items():
    cleaned_districts = {}
    for district, cities in districts.items():
        cleaned_districts[district] = sorted(list(set(cities)))
    cleaned_data[state] = cleaned_districts

with open('D:\\Coding\\Python\\api\\addrees\\combined_data_cleaned.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned_data, f, indent=2, ensure_ascii=False)