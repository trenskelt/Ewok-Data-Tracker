# Ewok Data Tracker - By Trent

# Store the main ewok info in the dictionary
ewok_data = {
    "name": "Wicket",
    "age": 25,
    "weapon": "Spear",
    "rank": "Warrior"
}

# Print the original ewok stuff
print("Ewok Name:", ewok_data["name"])
print("Ewok Age:", ewok_data["age"])
print("Ewok Weapon:", ewok_data["weapon"])
print("Ewok Rank:", ewok_data["rank"])

# Update the ewok info 
ewok_data["weapon"] = "12 Gauge + AR15"
ewok_data["rank"] = "BIG BAUS"
ewok_data["homeworld"] = "Chicago"

# Print updated ewok info
print("\nUpdated Ewok Data:")
for key, value in ewok_data.items():
    print(f"{key}: {value}")

# Create a group of fellers``
ewok_tribe = {
    "Wicket": ewok_data,
    "BIG BAUS": {
        "name": "El Presidente",
        "age": 30,
        "weapon": "Staff",
        "rank": "Chief",
        "homeworld": "Endor"
    }
}

# Print all the ewoks in one gang
print("\nEwok Tribe Data:")
for ewok_name, ewok_info in ewok_tribe.items():
    print(f"\nEwok: {ewok_name}")
    for key, value in ewok_info.items():
        print(f"{key}: {value}")


###### Pizza
