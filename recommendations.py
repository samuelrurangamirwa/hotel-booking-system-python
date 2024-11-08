from bookings import USER_BOOKINGS

HOTELS = [
    {'name': 'Hotel A', 'location': (1.2900, 36.8200), 'amenities': ['WiFi', 'Pool', 'Gym']},
    {'name': 'Hotel B', 'location': (1.2920, 36.8230), 'amenities': ['WiFi', 'Restaurant']},
    {'name': 'Hotel C', 'location': (1.2930, 36.8240), 'amenities': ['Pool', 'Bar']},
]

# Function to recommend hotels based on a user's previous bookings
def recommend_hotels(user):
    """Recommends hotels to the user based on their booking history."""
    
    # Simple logic: recommend hotels with amenities the user booked previously
    user_bookings = []
    if user in USER_BOOKINGS:
        user_bookings = USER_BOOKINGS[user]
    
    recommended_hotels = set()
    for booking in user_bookings:
        # Find hotels with similar amenities
        for hotel in HOTELS:
            if hotel['name'] != booking['hotel']:  # Exclude already booked hotels
                recommended_hotels.add(hotel['name'])

    return list(recommended_hotels)