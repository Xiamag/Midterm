
import random 

class Ticket:
    def __init__(self, seat_number, section, price):
        self.seat_number = seat_number
        self.section = section
        self.price = price

class Attendee:
    def __init__(self, name):
        self.name = name
        self.__tickets_list = []

    def add_ticket(self):
        self.__tickets_list.append(ticket_object)

    def show_tickets(self):
        print(f"Seat number: {self.seat_number}")
        print(f"Section: {self.section}")
        print(f"Price: {self.price}")
        
        total_cost = sum(self.price)
        return f"Total cost: {total_cost}"
    
    def show_most_expensive_ticket(self):
        most_expensive = max(tickets_dictionary)
        return f"{attendee_name}'s Most Expensive Ticket: {most_expensive})"

class VIPAttendee(Attendee):
    def __init__(self, name):
        super().__init__(name)
    
    def add_ticket(self):
        price = price * 0.85
        self.__tickets_list.append(ticket_object)
        print(f"{attendee_name} (VIP) received a 15% discount. Discounted price: {price}")


attendee_list = []
tickets_dictionary = {}

number_attendees = int(input("Enter the number of attendees: "))
for number in range(1, number_attendees +1):
    attendee_type = input(f"Is attendee #{number} a regular attendee or a VIP attendee? (Enter 'v' for VIP), 'r' or anything else for regular): ")
    attendee_name = input(f"Enter the attendee's name: ")
    if attendee_type == "v":
        attendee = VIPAttendee(attendee_name)
        attendee_list.append(attendee)
    else:
        attendee = Attendee(attendee_name)
        attendee_list.append(attendee)
    
    number_of_tickets = input(f"How many tickets does {attendee_name} want to buy? ")
    for ticket in number_of_tickets:
        seat_number = random.randint(1,10_000)
    
    while True:
        enter_section = str(input("Enter sections: (A, B, C or D): ")).lower()
        if enter_section == "a":
            price = 100.00
        elif enter_section == "b":
            price = 90.00
        elif enter_section == "c":
            price = 80.00
        elif enter_section == "d":
            price = 70.00
        else:
            print("Invalid section. Try again!")
            continue

        ticket_object = Ticket(seat_number, enter_section, price)
        ticket_object.add_ticket()
        ticket_object[number_of_tickets] = ticket_object
        number_of_tickets += 1

        print(f"{attendee_name} bought ticket for seat {seat_number} in section {enter_section} for ${price}")

        print(attendee.show_tickets())








