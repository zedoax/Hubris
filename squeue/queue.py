"""
Files: queue.py
    @date_modified - 03/08/18
    @author - Elijah Bendinsky
"""


class SQueue:
    """
    Class: SQueue
        Provides a clean implementation of basic queue functionality
    """

    def __init__(self):
        """
        Constructor:
                Creates an empty queue
        """
        self.players = []

    def enqueue(self, item):
        """
        Methods: enqueue
            Adds an item to the queue
        Args:
            item: item to be added to the queue
        Returns:
            None -- no return type
        """
        self.players.append(item)

    def dequeue(self, index):
        """
        Methods: dequeue
            Remove a player from the queue
            # Takes advantage of python's arrays-as-linked-list
        Args:
            index: index of item to be removed
        Returns:
            item -- item removed (default: None)
        """
        try:
            item = self.players.pop(index)
            return item
        except IndexError:
            return None

    def remove(self, index):
        """
        Methods: remove
        Args:
            index: index of item to remove
            # Aggressive as fuck
        Returns:
            None -- no return type
        """
        self.players.pop(index)

    def reconstitute(self, players):
        """
        Methods: reconstitute
            Given a list of players, add them all to the queue
        Args:
            players: list of players to add
        Returns:
            bool -- if succeeds (should never fail)
        """
        for player in players:
            self.players.append(player)
            return True
