"""The ticketlist module, containing the ticketlist object."""
# from collections import OrderedDict

class Ticketlist:
    """The ticketlist object."""

    def __init__(self, name):
        """Construct a new ticketlist."""
        self._name = name
        # for open tickets
        self._ticket_pool = []
        # for assigned tickets
        self._assigned_ticket_pool = []
        # id of the ticket
        self._initial_id = 0

    def open_ticket(self, ticket):
        """Add a new ticket to the ticketlist."""
        self._ticket_pool.append(ticket)

    def get_open_tickets(self):
        """Get a list of all open tickets in SIS."""
        return self._ticket_pool

    def get_assigned_tickets(self):
        """Get all assigned tickets."""
        return self._assigned_ticket_pool

    def get_all_tickets(self):
        """Get a list of all tickets (open and assigned) in SIS."""
        return self._ticket_pool + self._assigned_ticket_pool

    def get_ids(self):
        """Get id of the ticket."""
        self._initial_id += 1
        return self._initial_id

    def close_ticket(self, ticket_name):
        """Remove a ticket from SIS."""
        for i, ticket in enumerate(self._ticket_pool):
            if ticket.get_name() == ticket_name:
                del self._ticket_pool[i]
                print(f"The ticket '{ticket_name}' was closed.")
                return
        for i, ticket in enumerate(self._assigned_ticket_pool):
            if ticket.get_name() == ticket_name:
                del self._assigned_ticket_pool[i]
                print(f"The ticket '{ticket_name}' was closed.")
                return
        print(f"An ticket '{ticket_name}' was not found.")

    def has_ticket_titled(self, title):
        """Loop over all ticketlist and return True if the title matches."""
        for ticket in self._ticket_pool:
            if ticket.get_name() == title:
                return True
        return False

    def assign_ticket(self, assigned_ticket_id, assigned_person):
        """Assign ticket to the person and remove from open ticket."""
        for open_ticket in self._ticket_pool:
            # print("============")
            # print(assigned_ticket_id)
            # print(open_ticket.get_id())
            # print(str(open_ticket.get_id()) == str(assigned_ticket_id))
            # print("============")
            if str(open_ticket.get_id()) == str(assigned_ticket_id):
                open_ticket.assign_ticket_to_person(assigned_person)
                self._ticket_pool.remove(open_ticket)
                self._assigned_ticket_pool.append(open_ticket)

    def find_assigned_title_by_id(self, assigned_ticket_id):
        """Find the title of the assigned ticket."""
        for assign_ticket in self._assigned_ticket_pool:
            if str(assign_ticket.get_id()) == str(assigned_ticket_id):
                return assign_ticket.get_name()

    def has_id(self, index):
        """Loop over all ticketlist and return True if the id matches."""
        for ticket in self._ticket_pool:
            if ticket.get_id() == index:
                return True
        return False
