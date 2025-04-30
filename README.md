# Indian Cities Organized by State and District

This project provides a structured JSON file (`combined_data.json`) containing Indian city names grouped under their respective **states** and **districts**. It was generated using the [OpenCage Geocoding API](https://opencagedata.com/) by processing a large list of cities and organizing them into a nested dictionary format for easier use in projects like:

- Location filtering in apps
- Cascading dropdowns (State → District → City)
- Search optimization
- Administrative UI panels

---

## 📁 File Structure

```json
{
  "Maharashtra": {
    "Pune": ["Pune", "Wagholi", "Shivapur"],
    "Nagpur": ["Nagpur", "Wadi"]
  },
  "Tamil Nadu": {
    "Chennai": ["Chennai", "Avadi"]
  }
}
# indian-cities-by-state-district
