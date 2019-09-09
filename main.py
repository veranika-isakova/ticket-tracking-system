"""The main module of the application."""

import sys

from input_output.user_input import Input
from input_output.terminal_output import Output
from persons.person import Person
from collection.collection import Collection
from tickets.ticket import Ticket
from ticketlist.ticketlist import Ticketlist

def main():
    """Run the application."""
    print("Welcome to SIS.")

    collection = Collection("My SIS")
    ticketlist = Ticketlist("The tickets of SIS")

    while True:
        Output.print_bold("What would you like to do?")
        user_input = Input.get_input()

        if user_input == "create person":
            person_name = Input.get_person_name()
            person = Person(person_name)

            if not collection.has_person_named(person_name):
                collection.add_person(person)
                Output.print_bold(f"{person_name} has been created.")
            else:
                Output.print_error(
                    f"A person named {person_name} is already present. Please rename the person."
                )

        elif user_input == "list people":
            people = collection.get_people()
            if not people:
                Output.print_bold("There are no people in the collection.")
            else:
                Output.print_bold(f"These are the people known to the system:")
                for person in people:
                    print(f"- {person.get_name()}")

        elif user_input == "open ticket":
            ticket_title = Input.get_ticket_title()
            ticket_index = ticketlist.get_ids()
            ticket = Ticket(ticket_title, ticket_index, None)
            if not ticketlist.has_ticket_titled(ticket_title):
                ticketlist.open_ticket(ticket)
                Output.print_bold(f"A ticket '{ticket_title}' was created with ID {ticket_index}.")
            else:
                Output.print_error(
                    f"A ticket '{ticket_title}' is already present. Please rename the ticket."
                )
        elif user_input == "list open tickets":
            open_tickets = ticketlist.get_open_tickets()
            if not open_tickets:
                Output.print_bold("There are no open tickets in SIS.")
            else:
                Output.print_bold(f"These are open tickets are known to the system:")
                for open_ticket in open_tickets:
                    print(f"{open_ticket.get_id()}: {open_ticket.get_name()}")

        elif user_input == "assign ticket":
            assigned_ticket_id = Input.get_ticket_id()
            assignee_name = Input.get_person_to_assign()
            ticketlist.assign_ticket(assigned_ticket_id, assignee_name)
            assigned_title = ticketlist.find_assigned_title_by_id(assigned_ticket_id)
            Output.print_bold(f"Ticket '{assigned_title}' has been assigned to {assignee_name}.")

        elif user_input == "list all tickets":
            all_tickets = ticketlist.get_all_tickets()
            assigned_tickets = ticketlist.get_assigned_tickets()
            if not all_tickets:
                Output.print_bold("There are no tickets in SIS.")
            else:
                Output.print_bold(f"These tickets are known to the system:")
                for ticket in all_tickets:
                    if ticket in assigned_tickets:
                        print(f"{ticket.get_id()}: {ticket.get_name()} ({ticket.get_person()})")
                    else:
                        print(f"{ticket.get_id()}: {ticket.get_name()} (unassigned)")

        elif user_input == "close ticket":
            closed_ticket = Input.get_ticket_title()
            ticketlist.close_ticket(closed_ticket)

        elif user_input == "exit":
            sys.exit()


if __name__ == "__main__":
    main()
