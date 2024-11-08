USER_BOOKINGS = {}

def book_room(user, hotel_name, room_number):
    """Books a room for a user and marks it as unavailable."""
    if user not in USER_BOOKINGS:
        USER_BOOKINGS[user] = []

    booking = {'hotel': hotel_name, 'room': room_number}
    USER_BOOKINGS[user].append(booking)
    print(f"Room {room_number} at {hotel_name} booked for {user}.")

def show_booking_history(user):
    """Displays the booking history for a user."""
    if user in USER_BOOKINGS:
        print(f"{user}'s Booking History:")
        for booking in USER_BOOKINGS[user]:
            print(f"- {booking['room']} at {booking['hotel']}")
    else:
        print(f"No booking history found for {user}.")