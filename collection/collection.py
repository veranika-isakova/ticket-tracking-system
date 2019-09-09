"""The collection module, containing the collection object."""

class Collection:
    """The collection object."""

    def __init__(self, name):
        """Construct a new collection."""
        self._name = name
        self._people_pool = []

    def add_person(self, person):
        """Add a person to the collection."""
        self._people_pool.append(person)

    def get_people(self):
        """Get a list of all people in the collection."""
        return self._people_pool

    def has_person_named(self, name):
        """Loop over all collection and return True if the name matches."""
        for person in self._people_pool:
            if person.get_name() == name:
                return True
        return False
