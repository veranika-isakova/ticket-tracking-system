"""The input module, containing the input class."""

from input_output.terminal_output import Output

class Input:
    """The input class, containing functions related to user input."""

    valid_commands = [
        "create person",
        "list people",
        "open ticket",
        "close ticket",
        "assign ticket",
        "list open tickets",
        "list all tickets",
        "exit"
    ]

    @classmethod
    def get_person_name(cls):
        """Request the person name from the user."""
        Output.print_bold(f"What is the name of the person?")
        user_input = input()
        return user_input

    @classmethod
    def get_ticket_title(cls):
        """Request the ticket title from the user."""
        Output.print_bold(f"What is the title of the ticket?")
        user_input = input()
        return user_input

    @classmethod
    def get_ticket_id(cls):
        """Request the ticket id from the user."""
        Output.print_bold(f"What is the ticket id?")
        user_input = input()
        return user_input

    @classmethod
    def get_person_to_assign(cls):
        """Request the person name to assign it to the the ticket."""
        Output.print_bold(f"Who would you like to assign it to?")
        user_input = input()
        return user_input

    @classmethod
    def get_input(cls):
        """Get input from the command line and verfies its content."""
        user_input = input()
        if user_input not in cls.valid_commands:
            Output.print_error(f"'{user_input}' is an unknown command.")
            cls.print_help()
        return user_input

    @classmethod
    def print_help(cls):
        """Print a list of valid commands to stdout."""
        Output.print_bold("Valid commands:")
        for command in cls.valid_commands:
            print(command)
