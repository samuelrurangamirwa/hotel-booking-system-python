from hotels import find_nearest_hotel
from bookings import book_room, show_booking_history
from recommendations import recommend_hotels

def main():
    # Example user input for nearest hotel
    user_location = (1.2900, 36.8200)  # Latitude, Longitude for Kigali
    desired_amenities = ["WiFi", "Pool"]

    nearest_hotel = find_nearest_hotel(user_location, desired_amenities)
    print(f"Nearest hotel: {nearest_hotel['name']}")

    # Booking a room example
    user = "Samuel"
    hotel = nearest_hotel['name']
    room_number = 101
    book_room(user, hotel, room_number)

    # Display booking history for the user
    show_booking_history(user)

    # Get hotel recommendations for the user
    recommended_hotels = recommend_hotels(user)
    print(f"Recommended hotels for {user}: {recommended_hotels}")

if __name__ == "__main__":
    main()
