"""The ticket module, containing the Ticket object."""

class Ticket:
    """The ticket object."""

    def __init__(self, name, index, person):
        """Instantiate the ticket object and set the title of the ticket."""
        self._name = name
        self._index = index
        self._person = person

    def get_name(self):
        """Return the title of the ticket."""
        return self._name

    def get_id(self):
        """Return the id of the ticket."""
        return self._index

    def get_person(self):
        """Return the person of the ticket."""
        return self._person

    def assign_ticket_to_person(self, assigned_person):
        """Return the ticket assigned to person."""
        self._person = assigned_person
