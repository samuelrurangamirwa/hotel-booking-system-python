import random

# Sample data for hotels (In a real system, this data would come from a database)
HOTELS = [
    {'name': 'Hotel A', 'location': (1.2900, 36.8200), 'amenities': ['WiFi', 'Pool', 'Gym']},
    {'name': 'Hotel B', 'location': (1.2920, 36.8230), 'amenities': ['WiFi', 'Restaurant']},
    {'name': 'Hotel C', 'location': (1.2930, 36.8240), 'amenities': ['Pool', 'Bar']},
]

def find_nearest_hotel(user_location, desired_amenities):
    """Finds the nearest hotel to the user based on location and desired amenities."""
    
    def calculate_distance(loc1, loc2):
        # Simple placeholder function for calculating "distance" between two points
        # This would be replaced by a proper geolocation API or formula (like Haversine)
        return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])

    # Filter hotels based on desired amenities
    filtered_hotels = [
        hotel for hotel in HOTELS if all(amenity in hotel['amenities'] for amenity in desired_amenities)
    ]

    # Find the hotel with the minimum distance
    nearest_hotel = min(filtered_hotels, key=lambda hotel: calculate_distance(user_location, hotel['location']))
    return nearest_hotel
