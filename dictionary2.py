# Initialize the hotel room structure with rooms from 101 to 150
hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}
for room in range(100, 151):
    room_number = str(room)
    if room_number not in hotel_rooms:
        hotel_rooms[room_number] = {"status": "available", "customer": ""}

def book_room(room_number, customer_name):
    """Book a room and assign it to a customer."""
    if room_number in hotel_rooms:
        if hotel_rooms[room_number]["status"] == "available":
            hotel_rooms[room_number]["status"] = "booked"
            hotel_rooms[room_number]["customer"] = customer_name
            print(f"Room {room_number} has been booked for {customer_name}.")
        else:
            print(f"Room {room_number} is already booked.")
    else:
        print(f"Room {room_number} does not exist.")

def check_out(room_number):
    """Check out a customer and make the room available."""
    if room_number in hotel_rooms:
        if hotel_rooms[room_number]["status"] == "booked":
            customer_name = hotel_rooms[room_number]["customer"]
            hotel_rooms[room_number]["status"] = "available"
            hotel_rooms[room_number]["customer"] = ""
            print(f"Room {room_number} has been checked out by {customer_name}.")
        else:
            print(f"Room {room_number} is already available.")
    else:
        print(f"Room {room_number} does not exist.")

def display_status():
    """Display the status of all rooms."""
    print("Hotel Room Status:")
    for room_number, details in sorted(hotel_rooms.items()):
        status = details["status"]
        customer = details["customer"]
        print(f"Room {room_number}: {status}", end="")
        if status == "booked":
            print(f" (Customer: {customer})")
        else:
            print()

def main_menu():
    """Display the main menu and handle user choices."""
    while True:
        print("\nHotel Booking System Menu:")
        print("1. View current list of rooms and status")
        print("2. Book a room for a new customer")
        print("3. Check out of a room")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_status()
        elif choice == "2":
            room_number = input("Enter the room number: ")
            customer_name = input("Enter the customer name: ")
            book_room(room_number, customer_name)
        elif choice == "3":
            room_number = input("Enter the room number to check out: ")
            check_out(room_number)
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the main menu
main_menu()
