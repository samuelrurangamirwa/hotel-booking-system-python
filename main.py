from hotels import find_nearest_hotel
from bookings import book_room, show_booking_history
from recommendations import recommend_hotels

# List of valid amenities (this could be fetched dynamically from your hotel data)
VALID_AMENITIES = ["WiFi", "Pool", "Gym", "Restaurant", "Spa", "Parking"]

def main():
    while True:
        print("\nWelcome to the Hotel Booking System")
        
        # Get user input for location and desired amenities
        print("\nEnter your current location (latitude, longitude):")
        latitude = float(input("Latitude: "))
        longitude = float(input("Longitude: "))
        user_location = (latitude, longitude)

        print("\nEnter desired amenities (comma-separated, e.g., WiFi, Pool):")
        desired_amenities = input("Amenities: ").split(",")
        desired_amenities = [amenity.strip() for amenity in desired_amenities]  # Clean up extra spaces

        # Validate amenities
        invalid_amenities = [amenity for amenity in desired_amenities if amenity not in VALID_AMENITIES]
        if invalid_amenities:
            print(f"Warning: The following amenities are invalid and will be ignored: {', '.join(invalid_amenities)}")
            # Remove invalid amenities
            desired_amenities = [amenity for amenity in desired_amenities if amenity in VALID_AMENITIES]

        if not desired_amenities:
            print("No valid amenities selected. Please try again.")
            continue

        # Find the nearest hotel based on location and amenities
        nearest_hotel = find_nearest_hotel(user_location, desired_amenities)
        
        if not nearest_hotel:
            print("Sorry, no hotels found with the given criteria.")
            continue
        
        print(f"\nNearest hotel: {nearest_hotel['name']}")

        # Get user input for booking a room
        user = input("\nEnter your name: ")
        hotel = nearest_hotel['name']
        room_number = int(input(f"Enter room number to book at {hotel}: "))
        book_room(user, hotel, room_number)

        # Display booking history for the user
        show_booking_history(user)

        # Get hotel recommendations based on the user's booking history
        recommended_hotels = recommend_hotels(user)
        print(f"Recommended hotels for {user}: {recommended_hotels}")
        
        # Ask the user if they want to perform another action
        again = input("\nDo you want to book another room or get recommendations? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the Hotel Booking System! Goodbye.")
            break  # Exit the loop and end the program

if __name__ == "__main__":
    main()
