# Sample initial tickets
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(ticket_id, customer_name, issue_description):
    """Open a new service ticket."""
    if ticket_id in service_tickets:
        print(f"Ticket ID {ticket_id} already exists.")
    else:
        service_tickets[ticket_id] = {"Customer": customer_name, "Issue": issue_description, "Status": "open"}
        print(f"Ticket {ticket_id} opened for {customer_name} with issue: {issue_description}.")

def update_ticket_status(ticket_id, new_status):
    """Update the status of an existing ticket."""
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = new_status
        print(f"Ticket {ticket_id} status updated to {new_status}.")
    else:
        print(f"Ticket ID {ticket_id} does not exist.")

def display_tickets(filter_status=None):
    """Display all tickets, or filter by status if provided."""
    print("Service Tickets:")
    for ticket_id, details in sorted(service_tickets.items()):
        if filter_status is None or details["Status"] == filter_status:
            customer = details["Customer"]
            issue = details["Issue"]
            status = details["Status"]
            print(f"{ticket_id}: Customer: {customer}, Issue: {issue}, Status: {status}")

def main_menu():
    """Display the main menu and handle user choices."""
    while True:
        print("\nCustomer Service Ticket Tracker Menu:")
        print("1. View all tickets")
        print("2. View open tickets")
        print("3. View closed tickets")
        print("4. Open a new ticket")
        print("5. Update the status of a ticket")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            display_tickets()
        elif choice == "2":
            display_tickets(filter_status="open")
        elif choice == "3":
            display_tickets(filter_status="closed")
        elif choice == "4":
            ticket_id = input("Enter the new ticket ID: ")
            customer_name = input("Enter the customer name: ")
            issue_description = input("Enter the issue description: ")
            open_ticket(ticket_id, customer_name, issue_description)
        elif choice == "5":
            ticket_id = input("Enter the ticket ID: ")
            new_status = input("Enter the new status (open/closed): ")
            update_ticket_status(ticket_id, new_status)
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Run the main menu
main_menu()
