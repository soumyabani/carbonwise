def compute_carbon(data):
    kwh = data.get("electricity_kwh", 0)
    items = data.get("item_count", 0)
    distance = data.get("distance_km", 0)

    electricity = kwh * 0.4
    shopping = items * 0.3
    travel = distance * 0.18

    return {
        "electricity_kg": electricity,
        "shopping_kg": shopping,
        "travel_kg": travel,
        "total_kg": electricity + shopping + travel
    }

