"""
Class for a baby sitter
"""


class Sitter:
    """
    The payment due a sitter based upon the hours worked and the family they worked for
    """

    def __init__(self, start_time, hours_worked, family):
        """
        Constructor for Sitter class
        """

        self.start_time = start_time
        self.hours_worked = hours_worked
        self.family = family
