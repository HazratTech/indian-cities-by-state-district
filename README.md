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
```

## ☕ Support This Project

If this project helped you, consider supporting me:

[![Buy Me a Coffee](https://media.discordapp.net/attachments/659261445523111957/1367011496634093608/bmc-button.png?ex=6813082a&is=6811b6aa&hm=2383aa227bb9d618b888c8fffd50176ec157af785fefcda5d67cb16510ae4858&=&format=webp&quality=lossless)](https://www.buymeacoffee.com/hazratummar)


